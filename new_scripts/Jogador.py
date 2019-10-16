""" Nome do módulo :        Jogador
    Ano de criação :        2019/10
    Descrição do módulo :   Módulo que define a classe abstrata Jogador
    Versão :                2.0
    Pré-requisitos :        Agente
                            Ponto
    Membros :               Lorena Bassani
"""
from .Agente import Agente
from .geometria import Ponto

class Jogador(Agente):

    def __init__(self, idJ, ponto = Ponto(), comportamento = COMPORTAMENTOS.DEFESA):
        Agente.__init__(ponto)
        self.__id = idJ

    """ Nome da função :     id (getter)
        Intenção da função : Retorna o Id de um Jogador
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         Nenhum
        Retorno :            int : Id do joagador
    """
    @property
    def id(self):
        return self.__id

    """ Nome da função :     isInimigo
        Intenção da função : Dizer se o Jogador é Inimigo
        Pré-requisitos :     Ser uma subclasse de Joagador
        Efeitos colaterais : Nenhum
        Parâmetros :         Nenhum
        Retorno :            Boolean : True se for um Joagdor Inimigo, False caso contrário
    """
    def isInimigo(self):
        return NotImplementedError