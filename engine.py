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
        UI.falar("Olá jogador.")
        UI.esperar(1.0)
        UI.falar("É sua primeira vez jogando, certo?")

        opcoes1 = ["Sim", "Não"]
        while True:
            escolha = UI.menu(opcoes1)
            if escolha == 1:
                UI.falar("Entendo.")
                UI.esperar(1.0)
                UI.falar("Então antes de começarmos, vou te informar como essa visual novel vai funcionar.")
                UI.esperar(1.0)
                UI.falar("Vai seguir a vida de um estudante japonês do ensino médio.")
                UI.esperar(1.0)
                UI.falar("Vão ter alguns eventos ao longo da sua jogatina que irão influenciar na sua vida como estudante.")
                UI.esperar(1.0)
                UI.falar("O sistema de rotas vai ser definido com base na reputação que você tem com os personagens.")
                UI.esperar(1.0)
                UI.falar("E tenha em mente que toda ação que você faz tem um impacto em sua vida.")
                UI.esperar(1.0)
                UI.falar("Sabendo disso, pense bem antes de fazer certas escolhas.")
                UI.esperar(2.0)
                UI.falar("Bom, agora vamos continuar.")
                UI.esperar(2.0)
                UI.limpar_tela()
                break
            elif escolha == 2:
                UI.falar("Então espero que sua suposta experiência ajude daqui para frente.")
                UI.esperar(3.0)
                UI.limpar_tela()
                break
            else: 
                UI.falar("Responda adequadamente por favor.")
                UI.esperar(1.0)

        while True:
            UI.falar("Escolha um nome por favor.") 
            nome = UI.pedir_texto("> ")
            if len(nome) <= 15 and not nome.isnumeric():
                player.nome = nome # Salvando o nome no objeto Player
                break
            elif nome.isnumeric():
                UI.falar("Você é o R2D2?")
                UI.esperar(2.0) 
            else: 
                UI.falar("Talvez esse nome seja longo até demais.")
                UI.esperar(1.5)

        # Colocando cor APENAS no nome do jogador (Ciano)
        eu = f"\033[96m{player.nome}\033[0m"
        UI.falar(f"Certo, {eu}, vamos iniciar.")
        UI.esperar(2.0)
        UI.acao("...")
        UI.esperar(3.0)
        UI.limpar_tela()


class ChapterOneScene(Scene):
    def jogar(self, player):
        prima_nome = "Karina"
        
        # =========================================================
        # O SEGREDO AQUI: As variáveis já carregam a cor com elas!
        # \033[96m = Ciano | \033[95m = Magenta | \033[91m = Vermelho
        # \033[0m = Reseta a cor logo após o nome
        # =========================================================
        eu = f"\033[96m{player.nome}\033[0m"
        prima = f"\033[95m{prima_nome}\033[0m"
        misterio = f"\033[91m???\033[0m"
        
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
        UI.falar(f"{misterio}— {eu}?")
        UI.esperar(1.5)
        UI.falar(f"{misterio}: — Você vai chegar atrasado para seu primeiro dia de aula")
        UI.esperar(1.5)
        UI.falar("*Escuto ruídos barulhentos logo de manhã")
        UI.esperar(1.5)
        UI.falar("*Talvez seja melhor eu responder")
        UI.esperar(1.0)
        
        opcoes_acordar = ["Sim", "Não"]
        escolha_acordar = 0
        
        while True:
            escolha = UI.menu(opcoes_acordar)
            if escolha == 1:
                UI.falar(f"{eu}: *Boceja* — Já estou indo")
                UI.esperar(2.0)
                print("*Abrindo a porta*")
                UI.esperar(1.5)
                UI.falar(f"{misterio}:— Finalmente acordou, idiota")
                UI.esperar(1.5)
                UI.falar(f"{eu}:— Bom dia para você também, {prima}")
                UI.esperar(2.0)
                
                # Exemplo de uso de atributo de reputação se configurado no player
                if hasattr(player, 'reputacao_prima'):
                    player.reputacao_prima += 5 
                    
                escolha_acordar = 1
                break
            elif escolha == 2:
                UI.acao("...")
                UI.esperar(2.0)
                UI.falar("*CRASH*")
                UI.esperar(1.5)
                UI.falar(f"{misterio}:— ACORDA LOGO IDIOTA")
                UI.esperar(1.5)
                UI.falar(f"{eu}:— JÁ ESTOU INDO SUA MALUCA")
                UI.esperar(2.5)
                escolha_acordar = 2
                break
            else: 
                UI.falar("Responda adequadamente")
                UI.esperar(1.5)

        UI.falar("*Bom, vou começar a minha rotina de sempre")
        UI.esperar(1.5)
        UI.falar("*Mesmo sendo o ensino médio, não tenho muitas esperanças que vá mudar muita coisa")
        UI.esperar(1.0)
        UI.falar("*A vida não é igual os filmes, então vou ter que me esforçar mais do que eu gostaria")
        UI.esperar(1.0)
        UI.falar("*Porém talvez eu tenha uma pequena esperança que as coisas vão de algum jeito dar certo para mim agora.")
        UI.esperar(2.0)
        
        if escolha_acordar == 1:
            UI.falar(f"{prima}— Hoje você acordou mais rápido que o normal")
            UI.esperar(1.0)
            UI.falar(f"{prima}— Esta ansioso para sua jornada como aluno do ensino médio?")
            UI.esperar(1.5)
            UI.falar(f"{eu}— Não exatamente")
            UI.esperar(1.0)
            UI.falar(f"{eu}— Talvez eu só esteja me tornando alguém mais competente agora")
            UI.esperar(1.5)
            UI.falar(f"{prima}— Estou surpresa de escutar isso do mesmo cara que ficou coçando a bunda e jogando jogos as férias inteiras")
            UI.esperar(1.5)
            UI.falar(f"{eu}— Engraçado escutar isso da mesma pessoa que ficou na TV comendo todos os meus lanches o dia inteiro")
            UI.esperar(1.0)
            UI.falar(f"{eu}— Talvez até tenha ganhado alguns quilos")
            UI.esperar(1.5) 
            UI.falar(f"{prima}— Você está a fim de ir para seu primeiro dia de aula com o olho roxo?")
            UI.esperar(1.0)
            UI.falar(f"{prima}— Eu vou deixar essa passar só porque hoje é seu primeiro dia de aula")
            UI.esperar(1.5)
            UI.falar("*Após isso ela vai embora com uma leve expressão de raiva")
            UI.esperar(1.0)
            UI.falar("*O mais hilário disso é que ela realmente foi para o banheiro se pesar")

        elif escolha_acordar == 2:
            UI.falar(f"{prima}— Hoje é um dia importante para mim")
            UI.esperar(1.0)
            UI.falar(f"{prima}— Sua mãe me pediu para eu te acompanhar na escola até você conseguir se adaptar bem")
            UI.esperar(1.0)
            UI.falar(f"{prima}— Então por favor não vá me envergonhar logo hoje")
            UI.esperar(1.5)
            UI.falar(f"{eu}— Tá bom tá bom, vou tentar meu melhor")
            UI.esperar(1.5)
            UI.falar(f"{prima}— *Sigh*...Espero que você esteja levando isso a sério")
            UI.esperar(3.0)

        print("—" * 104)
        UI.falar(f"*Bom, esta é minha prima {prima}")
        UI.esperar(1.0)
        UI.falar("*O nome dela é meio incomum porque ela veio da europa")
        UI.esperar(1.0)
        UI.falar("*Meu tio ganhou uma bolsa lá e achou uma bela esposa")
        UI.esperar(1.0)
        UI.falar("*A esposa dele sempre teve interesse no japão, então eles decidiram se mudar para cá")
        UI.esperar(1.0)
        UI.falar(f"*Após isso eu conheci a {prima} com 6 anos de idade quando meu tio decidiu passar as férias na casa dos meus pais em Osaka")
        UI.esperar(1.0)
        UI.falar("*Na época...como posso dizer")
        UI.esperar(1.0)
        UI.falar("*Ela era uma criança com o espirito livre")
        UI.esperar(1.0)
        UI.falar("*Gostava de colecionar insetos e subir em árvores")
        UI.esperar(1.0)
        UI.falar("*Talvez esse seja o motivo que eu perdi um pouco de medo de insetos")
        UI.esperar(1.0)
        UI.falar("*De qualquer maneira, meu tio indicou uma escola interessante para eu fazer no ensino médio em Tóquio")
        UI.esperar(1.0)
        UI.falar("*Meus pais acharam a ideia interessante e foram na onda")
        UI.esperar(1.0)
        UI.falar("*Agora eu estou morando com meu tio, prima e sua esposa desde o começo das férias")
        UI.esperar(1.0)
        UI.falar("*Meu pai decidiu que eu deveria me mudar o mais rápido possível para me adaptar antes")
        UI.esperar(1.0)
        UI.falar("*Eu nunca tive muitos amigos no fundamental, então não tinha desculpas para me manter la de qualquer jeito")
        UI.esperar(1.0)
        UI.falar("*O ensino médio é uma virada de chave para muitas pessoas, então fiquei esperançoso que talvez algo dê certo para mim")
        UI.esperar(1.0)
        UI.falar("*Minha prima tem uma aparência acima da média, então acredito que ela não vai ter muitos problemas sobre isso")
        UI.esperar(1.0)
        UI.falar("*Porém eu sou uma pessoa totalmente mediana")
        UI.esperar(1.0)
        UI.falar("*E infelizmente essa é a realidade, pessoas como eu são socialmente excluídas")
        UI.esperar(1.0)
        UI.falar("*Quando eu me dei conta disso, eu já estava em Tóquio com todas as minhas bagagens na casa")
        UI.esperar(1.0)
        UI.falar(f"*Aparentemente a {prima} me falou que ia tomar conta de mim por um tempo")
        UI.esperar(1.0)
        UI.falar("*Mas não dou uma semana para ela ficar sem tempo para cuidar de seu pobre primo")
        UI.esperar(1.0)
        UI.falar("*Bom, vou terminar de me arrumar para não acabar me atrasando no primeiro dia")
        UI.esperar(4.0)
        print("—" * 104)
        UI.esperar(2.0)
        UI.falar(f"{prima}— Seu café está pronto")
        UI.esperar(1.0)
        UI.falar(f"{prima}— Minha mãe fritou alguns ovos antes de ir trabalhar")
        UI.esperar(1.5)
        UI.falar(f"{prima}— Coma rápido para nós sairmos no horario")
        UI.esperar(1.5)
        UI.falar(f"{eu}— Entendido")
        #Caminho escola
        print("—" * 104)
        UI.esperar(2.0)
        UI.falar("*No caminho da escola eu vi como a atmosfera em Tóquio é diferente")
        UI.esperar(1.0)
        UI.falar("*Da para ver como as pessoas não tem tempo para se preocupar com os outros")
        UI.esperar(2.0)

        escolha_comprar = 0
        opcoes_comprar = ["Lanche", "Bebida", "Marmita"]

        if escolha_acordar == 1:
            UI.falar(f"{prima}— Temos um pouco de tempo ainda, então vamos passar na loja de conveniencia antes")
            UI.esperar(1.0)
            UI.falar(f"{prima}— Você quer comprar alguma coisa?")
            UI.esperar(2.0)

            while True:
                escolha_comprar = UI.menu(opcoes_comprar)
                
                # Correção do loop infinito e da adição ao inventário (usando player em vez de Player)
                if 1 <= escolha_comprar <= len(opcoes_comprar):
                    item = opcoes_comprar[escolha_comprar - 1]
                    player.itens.append(item)
                    UI.falar(f"*Você comprou um(a) {item} e guardou na mochila.*")
                    UI.esperar(2.0)
                    break
                else:
                    UI.falar("Escolha inválida, tente de novo.")
                    UI.esperar(1.0)