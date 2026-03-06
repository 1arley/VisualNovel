import os
import sys
import time

class UI:
    @staticmethod
    def titulo(texto):
        print(30 * "=")
        print(texto)
        print(30 * "=")

    @staticmethod
    def menu(lista):
        for i, opcao in enumerate(lista):
            print(f"{i+1} - {opcao}")
        try:
            escolha = int(input("Escolha: "))
            return escolha
        except ValueError:
            return -1

    @staticmethod
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def falar(texto, velocidade=0.05):
        for caractere in texto:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(velocidade)
        print()

    @staticmethod
    def acao(texto, velocidade=0.5):
        # Reaproveitando a lógica do 'falar', mas permitindo velocidades diferentes
        UI.falar(texto, velocidade)