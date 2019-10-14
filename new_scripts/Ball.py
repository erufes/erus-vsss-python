from .Agente import Agente
from .geometria import Ponto

class Ball(Agente):

    def __init__(self, ponto = Ponto()):
        Agente.__init__(self, ponto)
