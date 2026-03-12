import os
from ui import UI
from player import Player

class Scene:
    """Classe base para todas as cenas do jogo."""
    def jogar(self, player):
        pass

class PrologueScene(Scene):
    def jogar(self, player):
        UI.acao("...")
        UI.esperar(2.0)
        UI.limpar_tela()
        UI.falar("Olá jogador.", cor="VERDE")
        UI.esperar(1.0)
        UI.falar("É sua primeira vez jogando, certo?", cor="VERDE")

        opcoes1 = ["Sim", "Não"]
        while True:
            escolha = UI.menu(opcoes1)
            if escolha == 1:
                UI.falar("Entendo.", cor="VERDE")
                UI.esperar(1.0)
                UI.falar("Então antes de começarmos, vou te informar como essa visual novel vai funcionar.", cor="VERDE")
                UI.esperar(1.0)
                UI.falar("Vai seguir a vida de um estudante japonês do ensino médio.", cor="VERDE")
                UI.esperar(1.0)
                UI.falar("Vão ter alguns eventos ao longo da sua jogatina que irão influenciar na sua vida como estudante.", cor="VERDE")
                UI.esperar(1.0)
                UI.falar("O sistema de rotas vai ser definido com base na reputação que você tem com os personagens.", cor="VERDE")
                UI.esperar(1.0)
                UI.falar("E tenha em mente que toda ação que você faz tem um impacto em sua vida.", cor="VERDE")
                UI.esperar(1.0)
                UI.falar("Sabendo disso, pense bem antes de fazer certas escolhas.", cor="VERDE")
                UI.esperar(2.0)
                UI.falar("Bom, agora vamos continuar.", cor="VERDE")
                UI.esperar(2.0)
                UI.limpar_tela()
                break
            elif escolha == 2:
                UI.falar("Então espero que sua suposta experiência ajude daqui para frente.", cor="VERDE")
                UI.esperar(3.0)
                UI.limpar_tela()
                break
            else: 
                UI.falar("Responda adequadamente por favor.", cor="VERMELHO")
                UI.esperar(1.0)

        while True:
            UI.falar("Escolha um nome por favor.", cor="VERDE") 
            nome = UI.pedir_texto("> ")
            if len(nome) <= 15 and not nome.isnumeric():
                player.nome = nome # Salvando o nome na instância do Player
                break
            elif nome.isnumeric():
                UI.falar("Você é o R2D2?", cor="AMARELO")
                UI.esperar(2.0) 
            else: 
                UI.falar("Talvez esse nome seja longo até demais.", cor="AMARELO")
                UI.esperar(2.5)

        UI.falar(f"Certo, {player.nome}, vamos iniciar.", cor="VERDE")
        UI.esperar(2.0)
        UI.acao("...")
        UI.esperar(3.0)
        UI.limpar_tela()


class ChapterOneScene(Scene):
    def jogar(self, player):
        prima = UI.falar("Karina", cor="AMARELO")
        
        # --- PARTE 1: O DESPERTAR ---
        UI.acao("DIA 1")
        UI.esperar(5.0)
        print("*TOK*"); UI.esperar(1.0); print("*TOK*")
        UI.esperar(3.0)
        UI.acao("...")
        UI.esperar(2.0)
        print("*TOK*"); UI.esperar(1.0); print("*TOK*"); UI.esperar(1.0); print("*TOK*")
        UI.esperar(2.0)
        
        UI.limpar_tela()
        UI.esperar(1.0)
        UI.falar(f"???— {player.nome}?", cor="VERMELHO")
        UI.esperar(1.5)
        UI.falar("???: — Você vai chegar atrasado para seu primeiro dia de aula", cor="VERMELHO")
        UI.esperar(1.5)
        UI.falar("*Escuto ruídos barulhentos logo de manhã*", cor="VERDE")
        UI.esperar(1.5)
        UI.falar("*Talvez seja melhor eu responder*", cor="VERDE")
        UI.esperar(1.0)
        
        opcoes_acordar = ["Responder com calma", "Gritar de volta"]
        escolha_acordar = 0
        
        while True:
            escolha = UI.menu(opcoes_acordar)
            if escolha == 1:
                UI.falar(f"{player.nome}: *Boceja* — Já estou indo", cor="CIANO")
                UI.esperar(2.0)
                UI.acao("*Abrindo a porta*")
                UI.esperar(1.5)
                UI.falar("???:— Finalmente acordou, idiota", cor="MAGENTA")
                UI.esperar(1.5)
                UI.falar(f"{player.nome}:— Bom dia para você também, {prima}", cor="CIANO")
                UI.esperar(2.0)
                
                if not hasattr(player, 'reputacao_prima'):
                    player.reputacao_prima = 0
                player.reputacao_prima += 5 
                    
                escolha_acordar = 1
                break
            elif escolha == 2:
                UI.acao("...")
                UI.esperar(2.0)
                UI.acao("*CRASH*")
                UI.esperar(1.5)
                UI.falar("???:— ACORDA LOGO IDIOTA", cor="VERMELHO")
                UI.esperar(1.5)
                UI.falar(f"{player.nome}:— JÁ ESTOU INDO SUA MALUCA", cor="CIANO")
                UI.esperar(2.5)
                escolha_acordar = 2
                break
            else: 
                UI.falar("Responda adequadamente", cor="AMARELO")
                UI.esperar(1.5)

        UI.falar("*Bom, vou começar a minha rotina de sempre*", cor="VERDE")
        UI.esperar(1.5)
        UI.falar("*Mesmo sendo o ensino médio, não tenho muitas esperanças que vá mudar muita coisa*", cor="VERDE")
        UI.esperar(1.0)
        
        # --- Caminho Escola e Loja de Conveniência ---
        UI.limpar_tela()
        UI.falar("*No caminho da escola eu vi como a atmosfera em Tóquio é diferente*", cor="VERDE")
        UI.esperar(1.0)
        UI.falar("*Dá para ver como as pessoas não têm tempo para se preocupar com os outros*", cor="VERDE")
        UI.esperar(2.0)

        escolha_comprar = 0
        opcoes_comprar = ["Lanche", "Bebida", "Marmita"]

        if escolha_acordar == 1:
            UI.falar(f"{prima}— Temos um pouco de tempo ainda, então vamos passar na loja de conveniência antes", cor="MAGENTA")
            UI.esperar(1.0)
            UI.falar(f"{prima}— Você quer comprar alguma coisa?", cor="MAGENTA")
            UI.esperar(2.0)

            while True:
                escolha_comprar = UI.menu(opcoes_comprar)
                
                if 1 <= escolha_comprar <= len(opcoes_comprar):
                    item_escolhido = opcoes_comprar[escolha_comprar - 1]

                    player.itens.append(item_escolhido)
                    
                    UI.falar(f"*Você comprou um(a) {item_escolhido} e guardou na mochila.*", cor="AMARELO")
                    print(f"\n[SISTEMA]: Novo item adicionado ao inventário: {item_escolhido}\n")
                    UI.esperar(2.0)
                    break 
                else:
                    UI.falar("Escolha inválida, a loja não tem isso.", cor="AMARELO")
                    UI.esperar(1.0)
                    
        UI.falar("Agora, preciso me concentrar em sobreviver ao primeiro dia de aula...", cor="VERDE")
        UI.esperar(3.0)
        UI.limpar_tela()