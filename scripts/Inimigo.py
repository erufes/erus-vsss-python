""" Nome do módulo :        Inimigo
    Ano de criação :        2019/10
    Descrição do módulo :   Módulo que especifica um inimigo em Campo
    Versão :                1.0
    Pré-requisitos :        Jogador
                            Ponto
    Membros :               Lorena Bassani
"""
from Jogador import Jogador
from Geometria import Ponto


class Inimigo(Jogador):

    def __init__(self, idJ, ponto=Ponto()):
        Jogador.__init__(self, idJ=idJ, ponto=ponto)

    """ Nome da função :     isInimigo
        Intenção da função : Dizer se um Jogador é Inimigo
        Pré-requisitos :     Ser uma Subclasse de Jogador
        Efeitos colaterais : Nenhum
        Parâmetros :         Nenhum
        Retorno :            Boolean : Sempre True
    """

    def isInimigo(self):
        return True
