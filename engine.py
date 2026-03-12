import time
from ui import UI
from player import Player

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
                player.nome = nome # Salvando o nome no objeto Player
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
        
        opcoes_acordar = ["Sim", "Não"]
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
                
                # Exemplo de uso de atributo de reputação se configurado no player
                if hasattr(player, 'reputacao_prima'):
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
        UI.falar("*A vida não é igual os filmes, então vou ter que me esforçar mais do que eu gostaria")
        time.sleep(1.0)
        UI.falar("*Porém talvez eu tenha uma pequena esperança que as coisas vão de algum jeito dar certo para mim agora.")
        time.sleep(2.0)
        
        if escolha_acordar == 1:
            UI.falar(f"{prima}— Hoje você acordou mais rápido que o normal")
            time.sleep(1.0)
            UI.falar(f"{prima}— Esta ansioso para sua jornada como aluno do ensino médio?")
            time.sleep(1.5)
            UI.falar(f"{player.nome}— Não exatamente")
            time.sleep(1.0)
            UI.falar(f"{player.nome}— Talvez eu só esteja me tornando alguém mais competente agora")
            time.sleep(1.5)
            UI.falar(f"{prima}— Estou surpresa de escutar isso do mesmo cara que ficou coçando a bunda e jogando jogos as férias inteiras")
            time.sleep(1.5)
            UI.falar(f"{player.nome}— Engraçado escutar isso da mesma pessoa que ficou na TV comendo todos os meus lanches o dia inteiro")
            time.sleep(1.0)
            UI.falar(f"{player.nome}— Talvez até tenha ganhado alguns quilos")
            time.sleep(1.5) 
            UI.falar(f"{prima}— Você está a fim de ir para seu primeiro dia de aula com o olho roxo?")
            time.sleep(1.0)
            UI.falar(f"{prima}— Eu vou deixar essa passar só porque hoje é seu primeiro dia de aula")
            time.sleep(1.5)
            UI.falar("*Após isso ela vai embora com uma leve expressão de raiva")
            time.sleep(1.0)
            UI.falar("*O mais hilário disso é que ela realmente foi para o banheiro se pesar")

        elif escolha_acordar == 2:
            UI.falar(f"{prima}— Hoje é um dia importante para mim")
            time.sleep(1.0)
            UI.falar(f"{prima}— Sua mãe me pediu para eu te acompanhar na escola até você conseguir se adaptar bem")
            time.sleep(1.0)
            UI.falar(f"{prima}— Então por favor não vá me envergonhar logo hoje")
            time.sleep(1.5)
            UI.falar(f"{player.nome}— Tá bom tá bom, vou tentar meu melhor")
            time.sleep(1.5)
            UI.falar(f"{prima}— *Sigh*...Espero que você esteja levando isso a sério")
            time.sleep(3.0)

        print("—" * 104)
        UI.falar(f"*Bom, esta é minha prima {prima}")
        time.sleep(1.0)
        UI.falar("*O nome dela é meio incomum porque ela veio da europa")
        time.sleep(1.0)
        UI.falar("*Meu tio ganhou uma bolsa lá e achou uma bela esposa")
        time.sleep(1.0)
        UI.falar("*A esposa dele sempre teve interesse no japão, então eles decidiram se mudar para cá")
        time.sleep(1.0)
        UI.falar(f"*Após isso eu conheci a {prima} com 6 anos de idade quando meu tio decidiu passar as férias na casa dos meus pais em Osaka")
        time.sleep(1.0)
        UI.falar("*Na época...como posso dizer")
        time.sleep(1.0)
        UI.falar("*Ela era uma criança com o espirito livre")
        time.sleep(1.0)
        UI.falar("*Gostava de colecionar insetos e subir em árvores")
        time.sleep(1.0)
        UI.falar("*Talvez esse seja o motivo que eu perdi um pouco de medo de insetos")
        time.sleep(1.0)
        UI.falar("*De qualquer maneira, meu tio indicou uma escola interessante para eu fazer no ensino médio em Tóquio")
        time.sleep(1.0)
        UI.falar("*Meus pais acharam a ideia interessante e foram na onda")
        time.sleep(1.0)
        UI.falar("*Agora eu estou morando com meu tio, prima e sua esposa desde o começo das férias")
        time.sleep(1.0)
        UI.falar("*Meu pai decidiu que eu deveria me mudar o mais rápido possível para me adaptar antes")
        time.sleep(1.0)
        UI.falar("*Eu nunca tive muitos amigos no fundamental, então não tinha desculpas para me manter la de qualquer jeito")
        time.sleep(1.0)
        UI.falar("*O ensino médio é uma virada de chave para muitas pessoas, então fiquei esperançoso que talvez algo dê certo para mim")
        time.sleep(1.0)
        UI.falar("*Minha prima tem uma aparência acima da média, então acredito que ela não vai ter muitos problemas sobre isso")
        time.sleep(1.0)
        UI.falar("*Porém eu sou uma pessoa totalmente mediana")
        time.sleep(1.0)
        UI.falar("*E infelizmente essa é a realidade, pessoas como eu são socialmente excluídas")
        time.sleep(1.0)
        UI.falar("*Quando eu me dei conta disso, eu já estava em Tóquio com todas as minhas bagagens na casa")
        time.sleep(1.0)
        UI.falar(f"*Aparentemente a {prima} me falou que ia tomar conta de mim por um tempo")
        time.sleep(1.0)
        UI.falar("*Mas não dou uma semana para ela ficar sem tempo para cuidar de seu pobre primo")
        time.sleep(1.0)
        UI.falar("*Bom, vou terminar de me arrumar para não acabar me atrasando no primeiro dia")
        time.sleep(4.0)
        print("—" * 104)
        time.sleep(2.0)
        UI.falar(f"{prima}— Seu café está pronto")
        time.sleep(1.0)
        UI.falar(f"{prima}— Minha mãe fritou alguns ovos antes de ir trabalhar")
        time.sleep(1.5)
        UI.falar(f"{prima}— Coma rápido para nós sairmos no horario")
        time.sleep(1.5)
        UI.falar(f"{player.nome}— Entendido")
        #Caminho escola
        print("—" * 104)
        time.sleep(2.0)
        UI.falar("*No caminho da escola eu vi como a atmosfera em Tóquio é diferente")
        time.sleep(1.0)
        UI.falar("*Da para ver como as pessoas não tem tempo para se preocupar com os outros")
        time.sleep(2.0)

        escolha_comprar = 0
        opcoes_comprar = ["Lanche", "Bebida", "Marmita"]


        if escolha_acordar == 1:
            UI.falar(f"{prima}— Temos um pouco de tempo ainda, então vamos passar na loja de conveniencia antes")
            time.sleep(1.0)
            UI.falar(f"{prima}— Você quer comprar alguma coisa?")
            time.sleep(2.0)

            while True:
                escolha_comprar = UI.menu(opcoes_comprar)
                Player.itens.append(escolha_comprar)
            