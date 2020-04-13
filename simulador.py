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
import Kernel
import Mundo
from enum import Enum


import Inimigo
from Aliado import Aliado
from ComportamentosJogadores.Factory import COMPORTAMENTOS


class Team(Enum):
    BLUE = 1
    YELLOW = 1


def main():
    print('Starting main...')
    print('Instantiating world...')
    mundo = Mundo.Mundo()  # noqa: F841
    time = [Aliado(0, comportamento=COMPORTAMENTOS.GOLEIRO), Aliado(1, comportamento=COMPORTAMENTOS.ATACANTE), Aliado(2)]
    inimigo = [Inimigo.Inimigo(3), Inimigo.Inimigo(4), Inimigo.Inimigo(5)]
    mundo.inimigos = inimigo
    mundo.time = time
    print('Done instatiating world')
    k = Kernel.Kernel()
    k.loop()
    print('Kernel started')


if __name__ == '__main__':
    main()
