""" VSSS-o-Primeiro
    Nome do módulo :        simulador
    Ano de criação :        2019/10
    Descrição do módulo:    Modulo para rodar o simulador no código do VSSS (segunda versão)
    Versão:                 2.0
    Pré-requisitos :        vsscorepy
    Membros:                Lorena Bassani
"""
import sys
sys.path.append('scripts')  # noqa: E402
from kernel import Kernel
from Mundo import Mundo
from enum import Enum


# from scripts.Inimigo import Inimigo
# from scripts.Aliado import Aliado
# from scripts.ComportamentosJogadores.Factory import COMPORTAMENTOS


class Team(Enum):
    BLUE = 1
    YELLOW = 1


def main():
    print('Starting main...')
    print('Instantiating world...')
    mundo = Mundo()  # noqa: F841
    print('Done instatiating world')
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
