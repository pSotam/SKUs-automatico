import random

lista_codigos = ["VF00150143", "VF00150189", "VF00W-8085", "VF00-POE32", "VF0098234", "VF00703140", "VF00700851",
                 "VF00700010", "VF00650615", "VF00650612", "VF00550108", "VF00550022", "VF00400046", "VF00350014",
                 "VF00321401", "VF00321220", "VF00200056", "VF00150072", "VF00150056", "VF00150052", "VF00150004",
                 "ACPX7"]

lista_usada = []

loops = int(input(f'Quantos SKUs pegar? (min: 1; max: {len(lista_codigos)}): '))

if(loops < 1 or loops > len(lista_codigos)):
    print('ERRO. TENTE NOVAMENTE!')
else:
    for i in range(loops):
        sku = random.choice(lista_codigos)
        lista_usada.append(sku)
        lista_codigos.remove(sku)
        print(sku)