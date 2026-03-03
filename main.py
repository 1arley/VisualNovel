import util
import time

def main():
    while True:
        util.limpar_tela()
        util.Titulo("Visual Novel 1")
        opcoes = ["Iniciar Jogo", "Carregar Jogo", "Sair"]
        escolha = util.MenuInicial(opcoes)
        
        if escolha == 1:
            print("Iniciando o jogo...")
        elif escolha == 2:
            print("Carregando o jogo...")
        elif escolha == 3:
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida!")
            time.sleep(2)


if __name__ == "__main__":
    main()