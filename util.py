import os

def Titulo(texto):
    print(30*"=")
    print(texto)
    print(30*"=")

def MenuInicial(lista):
    try:
        for i in range(len(lista)):
            print(f"{i+1} - {lista[i]}")
        escolha = int(input("Escolha: "))
        return escolha
    except ValueError:
        return -1

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

