import os
import sys
import time

# ==========================================
# MÓDULO: UI (Interface do Usuário)
# ==========================================
class UI:
    @staticmethod
    def titulo(texto):
        print(30 * "=")
        print(texto)
        print(30 * "=")

    @staticmethod
    def menu(lista):
        # DICA: Este menu é muito flexível. Você pode passar listas de qualquer tamanho.
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
        UI.falar(texto, velocidade)


# ==========================================
# MÓDULO: PLAYER (Jogador)
# ==========================================
class Player:
    def __init__(self):
        self.nome = ""
        # DICA: É aqui que o inventário do jogador vive. 
        # Você pode criar outros status aqui, como `self.dinheiro = 100` ou `self.reputacao = 0`
        self.itens = [] 


# ==========================================
# MÓDULO: ENGINE (Cenas e Lógica da História)
# ==========================================
class Scene:
    """Classe base para todas as cenas do jogo."""
    def jogar(self, player):
        pass

class PrologueScene(Scene):
    def jogar(self, player):
        UI.acao("...")
        time.sleep(2.0)
        UI.limpar_tela()
        UI.falar("Olá jogador.")
        time.sleep(1.0)
        UI.falar("É sua primeira vez jogando, certo?")

        opcoes1 = ["Sim", "Não"]
        while True:
            escolha = UI.menu(opcoes1)
            if escolha == 1:
                UI.falar("Entendo.")
                time.sleep(1.0)
                UI.falar("Então antes de começarmos, vou te informar como essa visual novel vai funcionar.")
                time.sleep(1.0)
                UI.falar("Vai seguir a vida de um estudante japonês do ensino médio.")
                time.sleep(1.0)
                UI.falar("Vão ter alguns eventos ao longo da sua jogatina que irão influenciar na sua vida como estudante.")
                time.sleep(1.0)
                # DICA: Como mencionado aqui, você pode adicionar variáveis no 'Player' para rastrear as rotas!
                UI.falar("O sistema de rotas vai ser definido com base na reputação que você tem com os personagens.")
                time.sleep(1.0)
                UI.falar("E tenha em mente que toda ação que você faz tem um impacto em sua vida.")
                time.sleep(1.0)
                UI.falar("Sabendo disso, pense bem antes de fazer certas escolhas.")
                time.sleep(2.0)
                UI.falar("Bom, agora vamos continuar.")
                time.sleep(2.0)
                UI.limpar_tela()
                break
            elif escolha == 2:
                UI.falar("Então espero que sua suposta experiência ajude daqui para frente.")
                time.sleep(3.0)
                UI.limpar_tela()
                break
            else: 
                UI.falar("Responda adequadamente por favor.")
                time.sleep(1.0)

        while True:
            UI.falar("Escolha um nome por favor.") 
            nome = input("> ")
            if len(nome) <= 15 and not nome.isnumeric():
                player.nome = nome # Salvando o nome na instância do Player
                break
            elif nome.isnumeric():
                UI.falar("Você é o R2D2?")
                time.sleep(2.0) 
            else: 
                UI.falar("Talvez esse nome seja longo até demais.")
                time.sleep(2.5)

        UI.falar(f"Certo, {player.nome}, vamos iniciar.")
        time.sleep(2.0)
        UI.acao("...")
        time.sleep(3.0)
        UI.limpar_tela()


class ChapterOneScene(Scene):
    def jogar(self, player):
        prima = "Karina"
        
        # --- PARTE 1: O DESPERTAR ---
        UI.acao("DIA 1")
        time.sleep(5.0)
        print("*TOK*"); time.sleep(1.0); print("*TOK*")
        time.sleep(3.0)
        UI.acao("...")
        time.sleep(2.0)
        print("*TOK*"); time.sleep(1.0); print("*TOK*"); time.sleep(1.0); print("*TOK*")
        time.sleep(2.0)
        
        UI.limpar_tela()
        time.sleep(1.0)
        UI.falar(f"???— {player.nome}?")
        time.sleep(1.5)
        UI.falar("???: — Você vai chegar atrasado para seu primeiro dia de aula")
        time.sleep(1.5)
        UI.falar("*Escuto ruídos barulhentos logo de manhã")
        time.sleep(1.5)
        UI.falar("*Talvez seja melhor eu responder")
        time.sleep(1.0)
        
        opcoes_acordar = ["Responder com calma", "Gritar de volta"]
        escolha_acordar = 0
        
        while True:
            escolha = UI.menu(opcoes_acordar)
            if escolha == 1:
                UI.falar(f"{player.nome}: *Boceja* — Já estou indo")
                time.sleep(2.0)
                print("*Abrindo a porta*")
                time.sleep(1.5)
                UI.falar("???:— Finalmente acordou, idiota")
                time.sleep(1.5)
                UI.falar(f"{player.nome}:— Bom dia para você também, {prima}")
                time.sleep(2.0)
                
                # DICA: Se você quiser um sistema de reputação, inicie ele no def __init__ da classe Player.
                if not hasattr(player, 'reputacao_prima'):
                    player.reputacao_prima = 0
                player.reputacao_prima += 5 
                    
                escolha_acordar = 1
                break
            elif escolha == 2:
                UI.acao("...")
                time.sleep(2.0)
                UI.falar("*CRASH*")
                time.sleep(1.5)
                UI.falar("???:— ACORDA LOGO IDIOTA")
                time.sleep(1.5)
                UI.falar(f"{player.nome}:— JÁ ESTOU INDO SUA MALUCA")
                time.sleep(2.5)
                escolha_acordar = 2
                break
            else: 
                UI.falar("Responda adequadamente")
                time.sleep(1.5)

        UI.falar("*Bom, vou começar a minha rotina de sempre")
        time.sleep(1.5)
        UI.falar("*Mesmo sendo o ensino médio, não tenho muitas esperanças que vá mudar muita coisa")
        time.sleep(1.0)
        
        # --- Caminho Escola e Loja de Conveniência ---
        UI.limpar_tela()
        UI.falar("*No caminho da escola eu vi como a atmosfera em Tóquio é diferente")
        time.sleep(1.0)
        UI.falar("*Dá para ver como as pessoas não têm tempo para se preocupar com os outros")
        time.sleep(2.0)

        escolha_comprar = 0
        opcoes_comprar = ["Lanche", "Bebida", "Marmita"]

        if escolha_acordar == 1:
            UI.falar(f"{prima}— Temos um pouco de tempo ainda, então vamos passar na loja de conveniência antes")
            time.sleep(1.0)
            UI.falar(f"{prima}— Você quer comprar alguma coisa?")
            time.sleep(2.0)

            while True:
                escolha_comprar = UI.menu(opcoes_comprar)
                
                # DICA: Verificação de segurança para saber se o jogador digitou um número válido (1, 2 ou 3)
                if 1 <= escolha_comprar <= len(opcoes_comprar):
                    # DICA: escolha_comprar é o número que o usuário digitou (1, 2 ou 3).
                    # Subtraímos 1 porque as listas em Python começam do índice 0.
                    item_escolhido = opcoes_comprar[escolha_comprar - 1]

                    player.itens.append(item_escolhido)
                    
                    UI.falar(f"*Você comprou um(a) {item_escolhido} e guardou na mochila.*")
                    print(f"\n[SISTEMA]: Novo item adicionado ao inventário: {item_escolhido}\n")
                    time.sleep(2.0)
                    break 
                else:
                    UI.falar("Escolha inválida, a loja não tem isso.")
                    time.sleep(1.0)
                    
        UI.falar("Agora, preciso me concentrar em sobreviver ao primeiro dia de aula...")
        time.sleep(3.0)
        UI.limpar_tela()

