""" Nome do módulo :        ComportamentoGoleiro
    Ano de criação :        2019/10
    Descrição do módulo :   Comportamento de Goleiro para Jogadores
    Versão :                1.0
    Pré-requisitos :        IComportamento
    Membros :               Lorena Bassani
"""
from .IComportamento import IComportamento

class ComportamentoGoleiro(IComportamento):
    def __init__(self):
        IComportamento.__init__(self)