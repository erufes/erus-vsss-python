from .padroes.Singleton import Singleton
from .Player import Player, COMPORTAMENTOS
from .Ball import Ball

class Mundo(Singleton):
    def __init__(self, ball):
        Singleton.__init__(self)
        self.__jogadores = {"Team" : list(), "Enemies" : list()}
        self.__ball = ball
    
    @property
    def inimigos(self):
        return self.__jogadores["Enemies"]
    
    @inimigos.setter
    def inimigos(self, inimigos):
        self.__jogadores["Enemies"].clear()
        self.__jogadores["Enemies"].extend(inimigos)
    
    @property
    def goleiro(self):
        g = list(filter(lambda x: x.comportamento == COMPORTAMENTOS.GOLEIRO, self.__jogadores["Team"]))
        if g: 
            return g[0]
        return None
    
    @goleiro.setter
    def goleiro(self, playerId):
        if not self.goleiro:
            p = player(playerId)
            p.comportamento = COMPORTAMENTOS.GOLEIRO
    
    def player(self, playerId):
        p = list(filter(lambda x: x.id == playerId, self.__jogadores["Team"]))
        if p:
            return p
        return None
