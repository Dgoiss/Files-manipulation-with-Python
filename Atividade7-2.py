import json

inventario = []

try:
    with open('inventario.json', 'r') as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError : inventario = []

def Adicionar():
    nome = input("Nome do produto: ")
    preco = float(input('Preco do produto: '))
    inventario.append({'Nome': nome, 'Preco': preco})

    with open('inventario.json', 'w') as arquivo:
        json.dump(inventario, arquivo, indent=4)

def Remover():
    nome = input("Nome do produto: ")

    novo_inventario = [item for item in inventario if item['Nome'] != nome]

    with open('inventario.json', 'w') as arquivo:
        json.dump(novo_inventario, arquivo)
    
    inventario[:] = novo_inventario

def Exibir():
    for i in range(len(inventario)):
        print(inventario[i])

def Menu():
    menu = True
    
    while menu == True:
        print("Selecione uma opcao: ")
        print("1 - Adicionar")
        print("2 - Remover")
        print("3 - Exibir")

        try:
            opcao = int(input('Opcao: '))
        except ValueError:
            print('!!Digite uma opcao valida!!')
            continue

        if(opcao == 1): Adicionar()
        elif (opcao == 2): Remover()
        elif(opcao == 3): Exibir()
        else: menu = False

Menu()