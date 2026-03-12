import os
from engine import UI, Player, PrologueScene, ChapterOneScene

class GameEngine:
    def __init__(self):
        self.player = Player()
        self.rodando = True
        self.cenas = [PrologueScene(), ChapterOneScene()]

    def iniciar(self):
        # A magia da pausa acontece ao ligar o sistema aqui:
        UI.iniciar_sistema_de_pause()
        
        while self.rodando:
            UI.limpar_tela()
            UI.titulo("Visual Novel 1")
            opcoes = ["Iniciar Jogo", "Carregar Jogo", "Sair"]
            escolha = UI.menu(opcoes)
            
            if escolha == 1:
                print("Iniciando o jogo...")
                UI.esperar(1.5)
                self.novo_jogo()
            elif escolha == 2:
                print("Carregando o jogo... (Sistema não implementado)")
                UI.esperar(2.0)
            elif escolha == 3:
                print("Saindo do jogo...")
                self.rodando = False
            else:
                print("Opção inválida!")
                UI.esperar(2.0)

    def novo_jogo(self):
        UI.limpar_tela()
        
        for cena in self.cenas:
            cena.jogar(self.player)
            
        UI.limpar_tela()
        UI.titulo("FIM DA DEMONSTRAÇÃO")
        
        print("\n=== SEU STATUS FINAL ===")
        print(f"Nome: {self.player.nome}")
        print(f"Inventário: {', '.join(self.player.itens) if self.player.itens else 'Vazio'}")
        print("========================\n")
        
        # O input seguro que permite apertar espaço no texto sem pausar o jogo atoa
        UI.pedir_texto("Pressione Enter para voltar ao menu...")

if __name__ == "__main__":
    jogo = GameEngine()
    jogo.iniciar()