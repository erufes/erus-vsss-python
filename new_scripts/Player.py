from .Agente import Agente
from .geometria import Ponto
from .ComportamentosJogadores import Comportamentos, Factory

class Player(Agente):

    def __init__(self, id, ponto = Ponto(), comportamento = COMPORTAMENTOS.DEFESA):
        Agente.__init__(poto)
        self.__id = id
        self.comportamento = comportamento
    
    @property
    def comportamento(self):
        return self.__comportamentoId
    
    @comportamento.setter
    def comportamento(self, comportamento):
        self.__comportamentoId = comportamento
        self.__comportamento = Factory.create(comportamento)
    
    @property
    def id(self):
        return self.__id