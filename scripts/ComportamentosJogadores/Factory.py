""" Nome do módulo :        Factory
    Ano de criação :        2019/10
    Descrição do módulo :   Fábrica de comportamentos de jogador
    Versão :                1.0
    Pré-requisitos :        Comportamentos
                            ComportamentoGoleiro
                            ComportamentoDefesa
                            ComportamentoAtaque
    Membros :               Lorena Bassani
"""
from .Comportamentos import COMPORTAMENTOS
from .ComportamentoGoleiro import ComportamentoGoleiro
from .ComportamentoDefesa import ComportamentoDefesa
from .ComportamentoAtacante import ComportamentoAtacante
from .ComportamentoLissajous import ComportamentoLissajous

class Factory(object):

    """ Nome da função :     create
        Intenção da função : Criar um objeto adequado de comportamento para Jogador
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         COMPORTAMENTO : Comportamento relativo ao que se quer do Jogador
        Retorno :            IComportamento : Objeto que implementa um Comportamento de Jogador
    """
    @staticmethod
    def create(comportamento):
        if comportamento == COMPORTAMENTOS.GOLEIRO:
            return ComportamentoGoleiro()
        elif comportamento == COMPORTAMENTOS.ATACANTE:
            return ComportamentoAtacante()
        elif comportamento == COMPORTAMENTOS.DEFESA:
            return ComportamentoDefesa()
        else:
            return ComportamentoLissajous()