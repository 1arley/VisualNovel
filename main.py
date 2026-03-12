import time
import os
from engine import UI, Player, PrologueScene, ChapterOneScene

class GameEngine:
    def __init__(self):
        self.player = Player()
        self.rodando = True
        # DICA: Para adicionar novos capítulos, crie a classe Herdando de Scene e adicione nesta lista!
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
        # DICA: O motor percorre a lista de cenas automaticamente.
        # Ele passa a mesma instância 'self.player' para todas as cenas, mantendo os itens e o nome salvos!
        for cena in self.cenas:
            cena.jogar(self.player)
            
        UI.limpar_tela()
        UI.titulo("FIM DA DEMONSTRAÇÃO")
        
        # Mostrando o inventário no final como teste:
        print("\n=== SEU STATUS FINAL ===")
        print(f"Nome: {self.player.nome}")
        print(f"Inventário: {', '.join(self.player.itens) if self.player.itens else 'Vazio'}")
        print("========================\n")
        
        input("Pressione Enter para voltar ao menu...")

# Execução do script principal
if __name__ == "__main__":
    jogo = GameEngine()
    jogo.iniciar()