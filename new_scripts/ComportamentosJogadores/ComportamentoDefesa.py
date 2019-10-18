""" Nome do módulo :        ComportamentoDefesa
    Ano de criação :        2019/10
    Descrição do módulo :   Comportamento de Defesa para Jogadores
    Versão :                1.0
    Pré-requisitos :        IComportamento
    Membros :               Lorena Bassani
"""
from .IComportamento import IComportamento

class ComportamentoDefesa(IComportamento):
    def __init__(self):
        IComportamento.__init__(self)