""" Nome do módulo :        Ball
    Ano de criação :        2019/10
    Descrição do módulo :   Módulo que define bola em campo
    Versão :                2.0
    Pré-requisitos :        Agente
                            Ponto
    Membros :               Lorena Bassani
"""
from .Agente import Agente
from .geometria import Ponto

class Ball(Agente):

    def __init__(self, ponto = Ponto()):
        Agente.__init__(self, ponto)
