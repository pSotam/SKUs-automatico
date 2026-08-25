from time import sleep


def linha():
    print("=" * 20)


def carregar_produtos(nome_arquivo):
    # Carrega a lista desejada
    with open(nome_arquivo, "r") as arquivo:
        produtos = [linha.strip() for linha in arquivo if linha.strip()]

    return produtos


def atualizar_arquivo(nome_arquivo, produtos):
    # Atualiza o arquivo desejado
    with open(nome_arquivo, "w") as arquivo:
        for produto in produtos:
            arquivo.write(produto + "\n")


def remover_duplicatas(produtos):
    # Remove SKUs duplicados da lista
    produtos_unicos = []
    produtos_duplicados = []

    for produto in produtos:
        if produto not in produtos_unicos:
            produtos_unicos.append(produto)

        else:
            print(
                f"({produto}) - ESTE ITEM É UMA DUPLICATA. "
                "REMOVENDO DA LISTA PRINCIPAL..."
            )

            sleep(0.05)
            produtos_duplicados.append(produto)

    return produtos_unicos, produtos_duplicados


def remover_enviados(produtos, enviados):
    # Remove SKUs que já foram enviados para reabastecimento
    produtos_filtrados = []
    produtos_apagados = []

    for produto in produtos:
        if produto in enviados:
            print(
                f"({produto}) - ESTE ITEM JÁ FOI ENVIADO. "
                "REMOVENDO DA LISTA PRINCIPAL..."
            )

            sleep(0.05)
            produtos_apagados.append(produto)

        else:
            produtos_filtrados.append(produto)

    return produtos_filtrados, produtos_apagados


def mostrar_resultado(produtos, duplicados, apagados, enviados):
    # Mostra o resultado e permite executar verificações que ainda não foram feitas

    linha()
    print("RESULTADO FINAL:")

    # Verificação de duplicatas
    if duplicados:
        print(f"Duplicatas removidas: {len(duplicados)}")

    else:
        print("Nenhuma duplicata encontrada.")
        print("// Deseja verificar se há algum SKU duplicado?")
        print("[ 1 ] Verificar")
        print("[ 2 ] Não verificar")

        verificar_se_duplicado = input("Escolha: ")

        if verificar_se_duplicado == "1":
            linha()
            print("VERIFICANDO SE HÁ DUPLICATAS:")

            produtos, duplicados = remover_duplicatas(produtos)

            atualizar_arquivo("produtos", produtos)

            print(f"PRODUTOS DUPLICADOS REMOVIDOS: {len(duplicados)}")

    # Verificação de itens já enviados
    if apagados:
        print(f"SKUs já enviados removidos: {len(apagados)}")

    else:
        print("Nenhum SKU já enviado encontrado")
        print("// Deseja verificar se há algum SKU já enviado?")
        print("[ 1 ] Verificar")
        print("[ 2 ] Não verificar")

        verificar_se_enviado = input("Escolha: ")

        if verificar_se_enviado == "1":
            linha()
            print(
                "VERIFICANDO SE ALGUM ITEM SEM ESTOQUE "
                "JÁ FOI ENVIADO PARA REABASTECER:"
            )

            produtos, apagados = remover_enviados(
                produtos,
                enviados
            )

            atualizar_arquivo("produtos", produtos)

            print(f"ITENS REMOVIDOS: {len(apagados)}")

    linha()
    print(f"Lista final de SKUs já disponível! ({len(produtos)})")
    linha()

    # Retorna os dados atualizados para o programa principal
    return produtos, duplicados, apagados


# PROGRAMA PRINCIPAL

produtos_sem_estoque = carregar_produtos("produtos")
produtos_enviados = carregar_produtos("enviados")

produtos_duplicados = []
produtos_apagados = []

programa = 0

while programa == 0:

    linha()

    print("     FILTRO DE SKUs     ")

    print(
        "FUNÇÕES DISPONÍVEIS:\n"
        "[ 1 ] Verificar duplicatas\n"
        "[ 2 ] Verificar itens já enviados\n"
        "[ 3 ] Ver lista final"
    )

    funcao = input("Escolha a função desejada: ")

    if funcao == "1":

        linha()
        print("VERIFICANDO SE HÁ DUPLICATAS:")

        produtos_sem_estoque, produtos_duplicados = remover_duplicatas(
            produtos_sem_estoque
        )

        atualizar_arquivo("produtos", produtos_sem_estoque)

        print(
            f"PRODUTOS DUPLICADOS REMOVIDOS: "
            f"{len(produtos_duplicados)}"
        )

    elif funcao == "2":

        linha()
        print(
            "VERIFICANDO SE ALGUM ITEM SEM ESTOQUE "
            "JÁ FOI ENVIADO PARA REABASTECER:"
        )

        produtos_sem_estoque, produtos_apagados = remover_enviados(
            produtos_sem_estoque,
            produtos_enviados
        )

        atualizar_arquivo("produtos", produtos_sem_estoque)

        print(f"ITENS REMOVIDOS: {len(produtos_apagados)}")

    elif funcao == "3":

        (
            produtos_sem_estoque,
            produtos_duplicados,
            produtos_apagados
        ) = mostrar_resultado(
            produtos_sem_estoque,
            produtos_duplicados,
            produtos_apagados,
            produtos_enviados
        )


#FAZER SISTEMA QUE COLOCA ESSES SKUs NA MENSAGEM FINAL
    #então meio que o sistema vai passando quais SKUs você realmente usou afinal e coloca numa mensagem
        #separado por: Comprar; Trazer de SCS.
