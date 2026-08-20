def linha():
    print('='*20)

with open("produtos", "r") as arquivo: #Pega a lista de SKUs sem estoque (atualizar sempre que usar)
    produtos_sem_estoque = [linha.strip() for linha in arquivo if linha.strip()]

with open("enviados", "r") as arquivo: #Pega a lista do que já foi enviado pra ser comprado
    produtos_enviados = [linha.strip() for linha in arquivo if linha.strip()]

def atualizar_arquivo(produtos):
    with open("produtos", "w") as arquivo:
        for produto in produtos:
            arquivo.write(produto + '\n')


produtos_filtrados = []
produtos_apagados = []




linha()
print('VERIFICANDO SE ALGUM ITEM SEM ESTOQUE JÁ FOI ENVIADO PARA REABASTECER:')

for SKU in produtos_sem_estoque: #verifica se o SKU sem estoque já foi enviado pra reabastecer antes.
    if SKU in produtos_enviados:
        print(f"({SKU}) - ESTE ITEM JÁ FOI ENVIADO. REMOVENDO DA LISTA PRINCIPAL.")
        produtos_apagados.append(SKU)
    else:
        produtos_filtrados.append(SKU)
print(f"ITENS REMOVIDOS: {len(produtos_apagados)}")
linha()

produtos_sem_estoque = produtos_filtrados

atualizar_arquivo(produtos_sem_estoque)

print(f'PRODUTOS SEM ESTOQUE ({len(produtos_sem_estoque)}):\n{produtos_sem_estoque}')
