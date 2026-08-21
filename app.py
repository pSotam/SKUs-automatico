from time import sleep

def linha():
    print("=" * 20)


def carregar_produtos(nome_arquivo): # Carrega a lista desejada (parametro nome_arquivo recebe nome da lista)
    with open(nome_arquivo, "r") as arquivo:
        produtos = [linha.strip() for linha in arquivo if linha.strip()]

    return produtos


def atualizar_arquivo(nome_arquivo, produtos): # Atualiza o arquivo desejado (nome_arquivo recebe nome da lista)
    with open(nome_arquivo, "w") as arquivo:
        for produto in produtos:
            arquivo.write(produto + "\n")


def remover_duplicatas(produtos): # Remove SKUs duplicados da lista final
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


def remover_enviados(produtos, enviados): # Remove SKUs que já foram enviados para serem reabastecidos
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


def mostrar_resultado(produtos, duplicados, apagados): # Mostra o resultado
    linha()
    print("RESULTADO FINAL:")

    if len(duplicados) > 0:
        print(f"Duplicatas removidas: {len(duplicados)}")

    if len(apagados) > 0:
        print(f"SKUs já enviados removidos: {len(apagados)}")

    linha()
    print(f"Lista final de SKUs já disponível! ({len(produtos)})")

    linha()


# PROGRAMA PRINCIPAL

produtos_sem_estoque = carregar_produtos("produtos")
produtos_enviados = carregar_produtos("enviados")

programa = 0
while programa == 0:
    linha()
    print('     FILTRO DE SKUs     ')
    print('FUNÇÕES DISPONÍVEIS:\n' \
    '[ 1 ] Verificar duplicatas\n' \
    '[ 2 ] Verificar itens já enviados\n' \
    '[ 3 ] Ver lista final')

    funcao = str(input('Escolha a função desejada: '))

    if(funcao == '1'):
        linha()
        print("VERIFICANDO SE HÁ DUPLICATAS:")

        produtos_sem_estoque, produtos_duplicados = remover_duplicatas(
            produtos_sem_estoque
        )

        atualizar_arquivo("produtos", produtos_sem_estoque)

        print(f"PRODUTOS DUPLICADOS REMOVIDOS: {len(produtos_duplicados)}")

    elif(funcao == '2'):
        linha()
        print("VERIFICANDO SE ALGUM ITEM SEM ESTOQUE JÁ FOI ENVIADO PARA REABASTECER:")

        produtos_sem_estoque, produtos_apagados = remover_enviados(
            produtos_sem_estoque,
            produtos_enviados
        )

        atualizar_arquivo("produtos", produtos_sem_estoque)

        print(f"ITENS REMOVIDOS: {len(produtos_apagados)}")

mostrar_resultado(
    produtos_sem_estoque,
    produtos_duplicados,
    produtos_apagados
)