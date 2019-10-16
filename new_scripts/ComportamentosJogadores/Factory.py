from .Comportamentos import COMPORTAMENTOS
from .ComportamentoGoleiro import ComportamentoGoleiro
from .ComportamentoDefesa import ComportamentoDefesa
from .ComportamentoAtacante import ComportamentoAtacante

class Factory(object):
    @staticmethod
    def create(comportamento):
        if comportamento == COMPORTAMENTOS.GOLEIRO:
            return ComportamentoGoleiro()
        elif comportamento == COMPORTAMENTOS.ATACANTE:
            return ComportamentoAtacante()
        else:
            return ComportamentoDefesa()