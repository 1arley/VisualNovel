import time
import util

def start():

    util.ActionSpeak_print("...")
    time.sleep(2.0)
    util.limpar_tela()
    util.Speak_print ("Olá jogador.")
    time.sleep(1.0)
    util.Speak_print("É sua primeira vez jogando, certo?")

    opcoes1 = ["sim", "não"]
    prima = "Karina"
    while True:

        escolha = util.MenuInicial(opcoes1)
        if escolha == 1:
            util.Speak_print("Entendo.")
            time.sleep(1.0)
            break
        elif escolha == 2:
            util.Speak_print("Então espero que sua suposta experiencia ajude daqui para frente.")
            time.sleep(1.0)
            break
        else: util.Speak_print("Responda adequadamente por favor."); time.sleep(1.0)
        

            
    
    while True:
        util.Speak_print("Escolha um nome por favor.") 
        nome = input("")
        if len(nome) <= 15:
            break
        elif nome.isnumeric():
            util.Speak_print("Você é o R2D2?")
            time.sleep(2.0) 
        else: 
            util.Speak_print("Talvez esse nome seja longo até demais.")
            time.sleep(2.5)

    util.Speak_print(f"Certo, {nome}, vamos iniciar")
    time.sleep(2.0)
    util.ActionSpeak_print("...")
    time.sleep(3.0)
    util.limpar_tela()

    print("*TOK*"); time.sleep(1.0); print("*TOK*")
    time.sleep(3.0)
    util.ActionSpeak_print("...")
    time.sleep(2.0)
    print("*TOK*"); time.sleep(1.0); print("*TOK*"); time.sleep(1.0); print("*TOK*")
    util.limpar_tela()
    time.sleep(1.0)
    util.Speak_print(f"{nome}?")
    time.sleep(1.0)
    util.Speak_print("???: — Você vai chegar atrasado para seu primeiro dia de aula")
    time.sleep(1.5)
    util.Speak_print("Escuto ruidos barulhentos logo de manhã")
    time.sleep(1.5)
    util.Speak_print("Talvez seja melhor eu responder")
    time.sleep(0.5)
    print("Responder?")

    while True:

        escolha = util.MenuInicial(opcoes1)
        if escolha == 1:
            util.Speak_print(f"{nome}: *Boceja* — Já estou indo")
            time.sleep(2.0)
            print("*Abrindo a porta*")
            time.sleep(1.5)
            util.Speak_print("???:— Finalmente acordou, idiota")
            util.Speak_print(f"{nome}:— Bom dia para você também, {prima}")
            time.sleep(2.0)
            break
        elif escolha == 2:
            util.ActionSpeak_print("...")
            util.Speak_print("*ESTRONDO*")
            util.Speak_print("???:— ACORDA LOGO IDIOTA")
            util.Speak_print(f"{nome}:— JÁ ESTOU INDO SUA MALUCA")
            break
        else: util.Speak_print("Responda adequadamente"); time.sleep(1.5)
    
    print("amo hitler")
    time.sleep(9.0)

        




