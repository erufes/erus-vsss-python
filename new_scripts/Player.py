from enum import Enum
from .Agente import Agente
from .geometria import Ponto

class COMPORTAMENTOS(Enum):
    GOLEIRO = 0
    ATACANTE = 1
    DEFESA = 2

class Player(Agente):

    def __init__(self, id, ponto = Ponto(), comportamento = COMPORTAMENTOS.DEFESA):
        Agente.__init__(poto)
        self.__id = id
        self.comportamento = comportamento
    
    @property
    def comportamento(self):
        return self.__comportamento
    
    @comportamento.setter
    def comportamento(self, comportamento):
        self.__comportamento = comportamento
    
    @property
    def id(self):
        return self.__id