import os
import sys
import time

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

def Speak_print(texto, velocidade=0.05):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()  # Força o Python a mostrar a letra agora
        time.sleep(velocidade)
    print()  # Pula linha ao final da frase

def ActionSpeak_print(texto, velocidade=0.5):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()  # Força o Python a mostrar a letra agora
        time.sleep(velocidade)
    print()  # Pula linha ao final da frase

