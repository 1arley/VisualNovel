from ui import UI
from player import Player
from engine import PrologueScene, ChapterOneScene
import time

class GameEngine:
    def __init__(self):
        self.player = Player()
        self.rodando = True
        # Aqui você define a ordem das cenas
        self.cenas = [PrologueScene(), ChapterOneScene()]

    def iniciar(self):
        while self.rodando:
            UI.limpar_tela()
            UI.titulo("Visual Novel 1")
            opcoes = ["Iniciar Jogo", "Carregar Jogo", "Sair"]
            escolha = UI.menu(opcoes)
            
            if escolha == 1:
                print("Iniciando o jogo...")
                time.sleep(1.5)
                self.novo_jogo()
            elif escolha == 2:
                print("Carregando o jogo... (Sistema não implementado)")
                time.sleep(2)
            elif escolha == 3:
                print("Saindo do jogo...")
                self.rodando = False
            else:
                print("Opção inválida!")
                time.sleep(2)

    def novo_jogo(self):
        UI.limpar_tela()
        # O motor do jogo percorre a lista de cenas automaticamente
        for cena in self.cenas:
            cena.jogar(self.player)
            
        UI.limpar_tela()
        UI.titulo("FIM DA DEMONSTRAÇÃO")
        input("Pressione Enter para voltar ao menu...")

if __name__ == "__main__":
    jogo = GameEngine()
    jogo.iniciar()