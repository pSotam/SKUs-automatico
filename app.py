with open("produtos", "r") as arquivo: #Pega a lista de SKUs sem estoque (atualizar sempre que usar)
    produtos_sem_estoque = [linha.strip() for linha in arquivo if linha.strip()]

print(produtos_sem_estoque)

with open("enviados", "r") as arquivo: #Pega a lista do que já foi enviado pra ser comprado
    produtos_enviados = [linha.strip() for linha in arquivo if linha.strip()]
print(produtos_enviados)



for i in range (len(produtos_enviados)): #vê se algum item na lista de produtos sem estoque já foi enviada antes
    if(i + 1 > len(produtos_sem_estoque)):
        break
    if produtos_sem_estoque[i] in produtos_enviados:
        print(f"({produtos_sem_estoque[i]}) - ESTE ITEM JÁ FOI ENVIADO. REMOVENDO DA LISTA PRINCIPAL.")
        produtos_sem_estoque.remove(produtos_sem_estoque[i])

print(produtos_sem_estoque)