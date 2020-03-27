""" VSSS-o-Primeiro
    Nome do módulo :        simulador
    Ano de criação :        2019/10
    Descrição do módulo:    Modulo para rodar o simulador no código do VSSS (segunda versão)
    Versão:                 2.0
    Pré-requisitos :        vsscorepy
    Membros:                Lorena Bassani
"""

from scripts.kernel import Kernel
# from scripts.Mundo import Mundo
# from scripts.Inimigo import Inimigo
# from scripts.Aliado import Aliado
# from scripts.ComportamentosJogadores.Factory import COMPORTAMENTOS

from enum import Enum
import math as m

class Team(Enum):
    BLUE = 1
    YELLOW = 1

def main():
    print('Starting main...')
    k = Kernel()
    k.loop()
    print('Kernel started')

# mundo = Mundo()
# time = [Aliado(0, comportamento = COMPORTAMENTOS.GOLEIRO), Aliado(1, comportamento = COMPORTAMENTOS.ATACANTE), Aliado(2)]
# inimigo = [Inimigo(3), Inimigo(4), Inimigo(5)]
# mundo.inimigos = inimigo
# mundo.time = time

if __name__ == '__main__':
    main()