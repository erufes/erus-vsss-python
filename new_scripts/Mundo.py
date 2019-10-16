""" Nome do módulo :        Mundo
    Ano de criação :        2019/10
    Descrição do módulo :   Módulo que define o Mundo onde ocorre o jogo
    Versão :                2.0
    Pré-requisitos :        Padrão Singleton
                            Jogador
                            Ball
                            ComportamentosJogadores Comportamentos
    Membros :               Lorena Bassani
"""
from .padroes.Singleton import Singleton
from .Jogador import Jogador
from .ComportamentosJogadores.Comportamentos import COMPORTAMENTOS
from .Ball import Ball

class Mundo(Singleton):
    def __init__(self, ball):
        Singleton.__init__(self)
        self.__jogadores = {"Team" : list(), "Enemies" : list()}
        self.__ball = ball
    
    """ Nome da função :     inimigos (getter)
        Intenção da função : Retorna os Inimigos
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         Nenhum
        Retorno :            list<Inimigos> : Lista de Inimigos
    """
    @property
    def inimigos(self):
        return self.__jogadores["Enemies"]
    
    """ Nome da função :     inimigos (setter)
        Intenção da função : Alterar a lista de inimigos
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Altera todo o time de inimigos
        Parâmetros :         Novo time de Inimigos
        Retorno :            Nenhum
    """
    @inimigos.setter
    def inimigos(self, inimigos):
        self.__jogadores["Enemies"].clear()
        self.__jogadores["Enemies"].extend(inimigos)
    
    """ Nome da função :     goleiro (getter)
        Intenção da função : Retorna o Jogador Goleiro
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         Nenhum
        Retorno :            Aliado : Jogador com Comportamento Goleiro
    """
    @property
    def goleiro(self):
        g = list(filter(lambda x: x.comportamento == COMPORTAMENTOS.GOLEIRO, self.__jogadores["Team"]))
        if g: 
            return g[0]
        return None
    
    """ Nome da função :     goleiro (setter)
        Intenção da função : Alterar o Goleiro
        Pré-requisitos :     Não ter um Goleiro previamente
        Efeitos colaterais : Define um novo goleiro
        Parâmetros :         int : Id do Jogador para alterar
        Retorno :            Nenhum
    """
    @goleiro.setter
    def goleiro(self, playerId):
        if not self.goleiro:
            p = player(playerId)
            p.comportamento = COMPORTAMENTOS.GOLEIRO
    
    """ Nome da função :     player (getter)
        Intenção da função : Retornar um Jogador de Acordo com seu Id
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         int : Id do Jogador
        Retorno :            Jogador : Jogador correspondente ao Id
    """
    def player(self, playerId):
        p = list(filter(lambda x: x.id == playerId, self.__jogadores["Team"]))
        if p:
            return p
        return None
