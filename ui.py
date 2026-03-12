import os
import sys
import time
from pynput import keyboard

class UI:
    pausado = False
    recebendo_input = False

    # Dicionário com os códigos ANSI das cores
    CORES = {
        "RESET": "\033[0m",
        "VERMELHO": "\033[91m",
        "VERDE": "\033[92m",
        "AMARELO": "\033[93m",
        "AZUL": "\033[94m",
        "MAGENTA": "\033[95m",
        "CIANO": "\033[96m",
        "BRANCO": "\033[97m"
    }

    @classmethod
    def ao_pressionar(cls, key):
        if key == keyboard.Key.space:
            if not cls.recebendo_input:
                cls.pausado = not cls.pausado
                if cls.pausado:
                    print("\n[⏸️ JOGO PAUSADO - Aperte ESPAÇO para continuar]", end="")
                    sys.stdout.flush()
                else:
                    print("\n[▶️ JOGO RETOMADO]")

    @classmethod
    def iniciar_sistema_de_pause(cls):
        listener = keyboard.Listener(on_press=cls.ao_pressionar)
        listener.start()

    @classmethod
    def checar_pause(cls):
        while cls.pausado:
            time.sleep(0.1)

    @classmethod
    def esperar(cls, segundos):
        tempo_decorrido = 0
        passo = 0.1
        while tempo_decorrido < segundos:
            cls.checar_pause()
            time.sleep(passo)
            tempo_decorrido += passo

    @classmethod
    def falar(cls, texto, velocidade=0.05, cor="RESET"):
        """Agora aceita uma cor! Se nenhuma for passada, usa a cor padrão do terminal."""
        cls.checar_pause()
        
        # Pega o código da cor no dicionário. Se o nome estiver errado, usa RESET.
        codigo_cor = cls.CORES.get(cor.upper(), cls.CORES["RESET"])
        
        # Ativa a cor no terminal
        sys.stdout.write(codigo_cor)
        
        for caractere in texto:
            cls.checar_pause()
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(velocidade)
            
        # Desativa a cor e pula para a próxima linha
        sys.stdout.write(cls.CORES["RESET"] + "\n")
        sys.stdout.flush()

    @classmethod
    def acao(cls, texto, velocidade=0.5, cor="AMARELO"):
        # Ações (como "DIA 1" ou reticências) podem ter uma cor padrão, como amarelo
        cls.falar(texto, velocidade, cor)

    @classmethod
    def menu(cls, lista):
        cls.recebendo_input = True 
        for i, opcao in enumerate(lista):
            print(f"{i+1} - {opcao}")
        try:
            escolha = int(input("Escolha: "))
            cls.recebendo_input = False 
            return escolha
        except ValueError:
            cls.recebendo_input = False
            return -1

    @classmethod
    def pedir_texto(cls, prompt="> "):
        cls.recebendo_input = True
        texto = input(prompt)
        cls.recebendo_input = False
        return texto

    @staticmethod
    def titulo(texto):
        print(30 * "=")
        print(texto)
        print(30 * "=")

    @staticmethod
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')