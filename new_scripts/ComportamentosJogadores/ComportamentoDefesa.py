""" Nome do módulo :        ComportamentoDefesa
    Ano de criação :        2019/10
    Descrição do módulo :   Comportamento de Defesa para Jogadores
    Versão :                1.0
    Pré-requisitos :        IComportamento
                            Geometria
                            Mundo, Arena, Lado
                            Jogador
                            Ball
                            math
    Membros :               Lorena Bassani
"""
from .IComportamento import IComportamento
from ..Geometria import Ponto
from ..Mundo import Mundo, Arena, Lado
from ..Jogador import Jogador
from ..Ball import Ball
import math as m

class ComportamentoDefesa(IComportamento):
    def __init__(self):
        IComportamento.__init__(self)

    def definirObjetivo(self, jogador, mundo):
        pass