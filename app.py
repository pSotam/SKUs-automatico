def linha():
    print('='*20)

with open("produtos", "r") as arquivo: #Pega a lista de SKUs sem estoque (atualizar sempre que usar)
    produtos_sem_estoque = [linha.strip() for linha in arquivo if linha.strip()]

with open("enviados", "r") as arquivo: #Pega a lista do que já foi enviado pra ser comprado
    produtos_enviados = [linha.strip() for linha in arquivo if linha.strip()]

def atualizar_sem_estoque(produtos):
    with open("produtos", "w") as arquivo:
        for produto in produtos:
            arquivo.write(produto + '\n')

'''print("COLE A LISTA DE SKU's ABAIXO:")
texto = str(input())
produtos_sem_estoque = texto.split(f"\n")
print(produtos_sem_estoque)'''


linha()
print('VERIFICANDO SE HÁ DUPLICATAS:')

produtos_unicos = []
produtos_duplicados = []

for i in produtos_sem_estoque: #Remove duplicatas
    if(i not in produtos_unicos):
        produtos_unicos.append(i)
    else:
        print(f"({i}) - ESTE ITEM É UMA DUPLICATA. REMOVENDO DA LISTA PRINCIPAL...")
        produtos_duplicados.append(i)
produtos_sem_estoque = produtos_unicos

print(f'PRODUTOS DUPLICADOS REMOVIDOS: {len(produtos_duplicados)}')

atualizar_sem_estoque(produtos_sem_estoque)


produtos_filtrados = []
produtos_apagados = []

linha()
print('VERIFICANDO SE ALGUM ITEM SEM ESTOQUE JÁ FOI ENVIADO PARA REABASTECER:')

for SKU in produtos_sem_estoque: #verifica se o SKU sem estoque já foi enviado pra reabastecer antes.
    if SKU in produtos_enviados:
        print(f"({SKU}) - ESTE ITEM JÁ FOI ENVIADO. REMOVENDO DA LISTA PRINCIPAL...")
        produtos_apagados.append(SKU)
    else:
        produtos_filtrados.append(SKU)
print(f"ITENS REMOVIDOS: {len(produtos_apagados)}")
linha()

produtos_sem_estoque = produtos_filtrados

atualizar_sem_estoque(produtos_sem_estoque)

print(f'PRODUTOS SEM ESTOQUE ({len(produtos_sem_estoque)}):\n{produtos_sem_estoque}')

linha()

#RESULTADO FINAL:

print('Resultado final:')

if(len(produtos_duplicados) > 0):
    print(f'Duplicatas removidas: {len(produtos_duplicados)}')
if(len(produtos_apagados) > 0):
    print(f'SKUs já enviados removidos: {len(produtos_apagados)}')

print(f'Lista de SKUs({len(produtos_sem_estoque)}):')
with open("produtos", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
