import time
from ui import UI

class Scene:
    """Classe base para todas as cenas do jogo."""
    def jogar(self, player):
        pass

class PrologueScene(Scene):
    def jogar(self, player):
        UI.acao("...")
        time.sleep(1.0)
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
                break
            elif escolha == 2:
                UI.falar("Então espero que sua suposta experiência ajude daqui para frente.")
                time.sleep(1.0)
                break
            else: 
                UI.falar("Responda adequadamente por favor.")
                time.sleep(1.0)

        while True:
            UI.falar("Escolha um nome por favor.") 
            nome = input("> ")
            if len(nome) <= 15 and not nome.isnumeric():
                player.nome = nome # Salvando o nome no objeto Player
                break
            elif nome.isnumeric():
                UI.falar("Você é o R2D2?")
                time.sleep(2.0) 
            else: 
                UI.falar("Talvez esse nome seja longo até demais.")
                time.sleep(2.0)

        UI.falar(f"Certo, {player.nome}, vamos iniciar.")
        time.sleep(2.0)
        UI.limpar_tela()

import time
from ui import UI

class ChapterOneScene(Scene):
    def jogar(self, player):
        prima = "Karina"
        
        # --- PARTE 1: O DESPERTAR ---
        print("*TOK*"); time.sleep(1.0); print("*TOK*")
        time.sleep(1.5)
        UI.acao("...")
        time.sleep(1.0)
        print("*TOK*"); time.sleep(1.0); print("*TOK*"); time.sleep(1.0); print("*TOK*")
        
        UI.limpar_tela()
        UI.falar(f"{player.nome}?")
        time.sleep(1.0)
        UI.falar(f"{prima}: — Você vai chegar atrasado para seu primeiro dia de aula!")
        time.sleep(1.5)
        UI.falar("Escuto ruídos barulhentos logo de manhã...")
        UI.falar("Talvez seja melhor eu responder antes que ela arrombe a porta.")
        
        opcoes_acordar = ["Responder com calma", "Gritar de volta"]
        while True:
            escolha = UI.menu(opcoes_acordar)
            if escolha == 1:
                UI.falar(f"{player.nome}: *Boceja* — Já estou indo.")
                time.sleep(2.0)
                print("*Abrindo a porta*")
                time.sleep(1.5)
                UI.falar(f"{prima}: — Finalmente acordou, idiota.")
                UI.falar(f"{player.nome}: — Bom dia para você também, {prima}.")
                break
            elif escolha == 2:
                UI.acao("...")
                UI.falar("*ESTRONDO*")
                UI.falar(f"{prima}: — ACORDA LOGO IDIOTA!")
                UI.falar(f"{player.nome}: — JÁ ESTOU INDO SUA MALUCA!")
                break
            else: 
                UI.falar("Responda adequadamente.")
                time.sleep(1.5)

        time.sleep(2.0)
        UI.limpar_tela()

        # --- PARTE 2: A CORRIDA E A AMIGA DE INFÂNCIA ---
        UI.falar("Me arrumo o mais rápido que posso, coloco o uniforme de qualquer jeito.")
        UI.falar("Pego uma fatia de pão de forma na cozinha e saio correndo com ela na boca.")
        UI.falar("É um clichê terrível, eu sei. Mas estou realmente atrasado.")
        time.sleep(2.0)
        
        UI.limpar_tela()
        UI.acao("*Passos rápidos na calçada*")
        time.sleep(1.0)
        UI.falar("Enquanto corro dobrando a esquina perto de casa, vejo uma figura familiar.")
        time.sleep(1.0)
        UI.falar("Uma garota com um laço vermelho no cabelo está parada, batendo o pé impaciente.")
        time.sleep(1.5)
        
        amiga = "Luana"
        UI.falar(f"{amiga}: — Atrasado de novo, hein?")
        UI.falar(f"{player.nome}: — {amiga}?! Você não foi pra escola ainda? Vai se atrasar também!")
        UI.falar(f"{amiga}: — Eu prometi que ia te esperar no primeiro dia, idiota! Vamos logo!")
        UI.falar(f"{amiga}: — Eu precisava garantir que você não ia fugir da nossa promessa! Vamos!")
        time.sleep(2.0)
        
        UI.limpar_tela()
        UI.falar("Luana é minha amiga de infância. Ela é a presidente (e única membra ativa) do Clube de Jornalismo.")
        UI.falar("Enquanto caminhamos apressados, ela já liga a câmera e aponta pra mim.")
        time.sleep(2.0)
        
        UI.falar(f"{amiga}: — Então, {player.nome}, preparado para investigar o prédio antigo depois da aula?")
        UI.falar(f"{player.nome}: — Prédio antigo? Achei que a gente ia só organizar os arquivos do clube...")
        UI.falar(f"{amiga}: — Mudei de ideia! Tem um boato sobre estática nos monitores da sala 404.")
        UI.falar(f"{amiga}: — Eu preciso de um cinegrafista... e de alguém pra ir na frente caso apareça algo bizarro.")
        
        opcoes_clube = ["Aceitar o destino", "Tentar pular fora"]
        while True:
            escolha = UI.menu(opcoes_clube)
            if escolha == 1:
                UI.falar(f"{player.nome}: — Tá bom, eu vou. Mas se a gente for pego pela zeladoria, a culpa é sua.")
                UI.falar(f"{amiga}: — Hehe! Sabia que podia contar com você!")
                break
            elif escolha == 2:
                UI.falar(f"{player.nome}: — Luana, você sabe que é proibido ir lá. Além disso, eu tenho que estudar...")
                UI.falar(f"{amiga}: *Faz bico* — Mentiroso! Você prometeu! Eu sou muito medrosa pra ir sozinha!")
                UI.falar(f"{player.nome}: — *Suspiro*... Tá bom, tá bom. Eu vou com você.")
                break
            else:
                UI.falar("Responda adequadamente.")
                time.sleep(1.5)

        time.sleep(2.0)
        UI.limpar_tela()

        # --- PARTE 3: O ITEM MISTERIOSO (SISTEMA DE INVENTÁRIO) ---
        UI.falar("Chegamos nos portões da escola justos no momento em que o sinal toca.")
        UI.falar("Enquanto Luana corre na frente para a sala dela, noto algo brilhando no chão perto dos armários.")
        time.sleep(1.5)
        
        UI.acao("*Você se abaixa para pegar o objeto*")
        UI.falar("É um pequeno pingente prateado com um formato estranho, quase como um olho.")
        UI.falar("Não parece pertencer a nenhum aluno comum.")
        
        # Adicionando o item ao inventário do jogador (POO em ação!)
        novo_item = "Pingente Prateado"
        player.itens.append(novo_item)
        
        print(f"\n[SISTEMA]: Novo item adicionado ao inventário: {novo_item}\n")
        time.sleep(2.5)
        
        UI.falar("Guardo o pingente no bolso. Talvez eu descubra de quem é mais tarde.")
        UI.falar("Agora, preciso me concentrar em sobreviver ao primeiro dia de aula...")
        time.sleep(3.0)
        UI.limpar_tela()