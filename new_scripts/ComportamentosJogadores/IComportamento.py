""" Nome do módulo :        IComportamento
    Ano de criação :        2019/10
    Descrição do módulo :   Interface de Comportamento para Padrão Strategy
    Versão :                1.0
    Pré-requisitos :        Nenhum
    Membros :               Lorena Bassani
"""
class IComportamento(object):
    def definirObjetivo(self, jogador, mundo):
        raise NotImplementedError