from time import sleep


def linha():
    print("=" * 20)


def carregar_produtos(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        produtos = [linha.strip() for linha in arquivo if linha.strip()]
    return produtos


def atualizar_arquivo(nome_arquivo, produtos):
    with open(nome_arquivo, "w") as arquivo:
        for produto in produtos:
            arquivo.write(produto + "\n")


def remover_duplicatas(produtos):
    produtos_unicos = []
    produtos_duplicados = []

    for produto in produtos:
        if produto not in produtos_unicos:
            produtos_unicos.append(produto)
        else:
            print(f"({produto}) - ESTE ITEM É UMA DUPLICATA. REMOVENDO DA LISTA PRINCIPAL...")
            sleep(0.05)
            produtos_duplicados.append(produto)

    return produtos_unicos, produtos_duplicados


def remover_enviados(produtos, enviados):
    produtos_filtrados = []
    produtos_apagados = []

    for produto in produtos:
        if produto in enviados:
            print(f"({produto}) - ESTE ITEM JÁ FOI ENVIADO. REMOVENDO DA LISTA PRINCIPAL...")
            sleep(0.05)
            produtos_apagados.append(produto)
        else:
            produtos_filtrados.append(produto)

    return produtos_filtrados, produtos_apagados


def mostrar_resultado(produtos, duplicados, apagados, enviados):
    linha()
    print("RESULTADO FINAL:")

    if duplicados:
        print(f"Duplicatas removidas: {len(duplicados)}")
    else:
        print("Nenhuma duplicata encontrada.")
        print("// Deseja verificar se há algum SKU duplicado?")
        print("[ 1 ] Verificar\n[ 2 ] Não verificar")

        if input("Escolha: ") == "1":
            linha()
            print("VERIFICANDO SE HÁ DUPLICATAS:")
            produtos, duplicados = remover_duplicatas(produtos)
            atualizar_arquivo("produtos", produtos)
            print(f"PRODUTOS DUPLICADOS REMOVIDOS: {len(duplicados)}")

    if apagados:
        print(f"SKUs já enviados removidos: {len(apagados)}")
    else:
        print("Nenhum SKU já enviado encontrado")
        print("// Deseja verificar se há algum SKU já enviado?")
        print("[ 1 ] Verificar\n[ 2 ] Não verificar")

        if input("Escolha: ") == "1":
            linha()
            print("VERIFICANDO SE ALGUM ITEM SEM ESTOQUE JÁ FOI ENVIADO PARA REABASTECER:")
            produtos, apagados = remover_enviados(produtos, enviados)
            atualizar_arquivo("produtos", produtos)
            print(f"ITENS REMOVIDOS: {len(apagados)}")

    linha()
    print(f"Lista final de SKUs já disponível! ({len(produtos)})")
    linha()

    return produtos, duplicados, apagados


# ---- SISTEMA DE MENSAGEM FINAL ----

def escolher_reabastecimento(sku):
    """Pergunta onde buscar o produto e retorna 'trazer' ou 'comprar'."""
    print('Onde pegar produto?\n'
          '[ 1 ] - São Caetano (SCS)\n'
          '[ 2 ] - Comprar')
    movimentacao = str(input('Escolha como reabastecer: ')).strip()

    if movimentacao == "1":
        return "trazer"
    elif movimentacao == "2":
        return "comprar"
    else:
        print('ERRO: OPÇÃO NÃO ENCONTRADA\nADICIONANDO À LISTA PARA COMPRAR')
        return "comprar"


def classificar_skus():
    """Pede ao usuário, um a um, os SKUs que serão enviados e separa entre trazer/comprar."""
    codigos_utilizados = []
    trazer = []
    comprar = []
    contador = 0

    while True:
        contador += 1
        print('APERTE ENTER PARA FECHAR')

        sku_utilizado = str(input(f"Digite o {contador}º SKU que vai ser enviado: ")).strip()

        if sku_utilizado == "":
            break

        destino = escolher_reabastecimento(sku_utilizado)

        if destino == "trazer":
            trazer.append(sku_utilizado)
        else:
            comprar.append(sku_utilizado)

        codigos_utilizados.append(sku_utilizado)

    return codigos_utilizados, trazer, comprar


def pedir_mensagem_personalizada():
    return str(input('\nDigite uma mensagem personalizada para a mensagem final (ou Enter para pular): ')).strip()


def exibir_relatorio(trazer, comprar, mensagem_personalizada):
    linha()
    print('Segue a lista de produtos para serem reabastecidos:')

    if trazer:
        print('Trazer de São Caetano:')
        for i, sku in enumerate(trazer):
            print(f"{i + 1} - {sku}")

    if comprar:
        print('Comprar:')
        for i, sku in enumerate(comprar):
            print(f"{i + 1} - {sku}")

    if mensagem_personalizada:
        print(mensagem_personalizada)
    linha()


def gerar_mensagem_final(produtos_sem_estoque):
    codigos_utilizados, trazer, comprar = classificar_skus()
    mensagem_personalizada = pedir_mensagem_personalizada()
    exibir_relatorio(trazer, comprar, mensagem_personalizada)


# ---- PROGRAMA PRINCIPAL ----

def main():
    produtos_sem_estoque = carregar_produtos("produtos")
    produtos_enviados = carregar_produtos("enviados")

    produtos_duplicados = []
    produtos_apagados = []

    while True:
        linha()
        print("     FILTRO DE SKUs     ")
        print(
            "FUNÇÕES DISPONÍVEIS:\n"
            "[ 1 ] Verificar duplicatas\n"
            "[ 2 ] Verificar itens já enviados\n"
            "[ 3 ] Ver lista final\n"
            "[ 4 ] Finalizar e gerar mensagem\n"
            "[ 5 ] Sair sem gerar mensagem"
        )

        funcao = input("Escolha a função desejada: ")

        if funcao == "1":
            linha()
            print("VERIFICANDO SE HÁ DUPLICATAS:")
            produtos_sem_estoque, produtos_duplicados = remover_duplicatas(produtos_sem_estoque)
            atualizar_arquivo("produtos", produtos_sem_estoque)
            print(f"PRODUTOS DUPLICADOS REMOVIDOS: {len(produtos_duplicados)}")

        elif funcao == "2":
            linha()
            print("VERIFICANDO SE ALGUM ITEM SEM ESTOQUE JÁ FOI ENVIADO PARA REABASTECER:")
            produtos_sem_estoque, produtos_apagados = remover_enviados(produtos_sem_estoque, produtos_enviados)
            atualizar_arquivo("produtos", produtos_sem_estoque)
            print(f"ITENS REMOVIDOS: {len(produtos_apagados)}")

        elif funcao == "3":
            produtos_sem_estoque, produtos_duplicados, produtos_apagados = mostrar_resultado(
                produtos_sem_estoque, produtos_duplicados, produtos_apagados, produtos_enviados
            )

        elif funcao == "4":
            gerar_mensagem_final(produtos_sem_estoque)
            break

        elif funcao == "5":
            print("Saindo sem gerar mensagem.")
            break

        else:
            print("ERRO: OPÇÃO NÃO ENCONTRADA")


if __name__ == "__main__":
    main()
    