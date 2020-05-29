""" Nome do módulo :      Agente
    Ano de criação :      2019/10
    Descrição do módulo : Agente representa uma entidade em campo
    Versão :              2.0
    Pré-requisitos :      sklearn
                          geometria
    Membros :             Lorena Bassani
"""
# from sklearn.linear_model import LinearRegression

from Geometria import Ponto
from Campo import Campo
from typing import List
# import math as m


class Agente(object):

    def __init__(self, ponto: Ponto = Ponto()):
        self._ponto: Ponto = ponto
        self._theta: float = 0
        self._posicoesAntigas: List[Ponto] = list()

    @property
    def ponto(self):
        return self._ponto

    @ponto.setter
    def ponto(self, value: Ponto):
        self.__changePosition(value)
        self._ponto = value
        # ?????
        c = Campo()
        c.occupy(c.transform2Grid((value.x, value.y)), self)

    @property
    def posicao(self):
        return self._ponto.posicao

    @posicao.setter
    def posicao(self, value):
        self._changePosition()
        self._ponto.posicao = value
        # ?????
        c = Campo()
        c.occupy(c.transform2Grid(value), self)

    @property
    def x(self):
        return self._ponto.x

    @property
    def y(self):
        return self._ponto.y

    @property
    def theta(self):
        return self._theta

    @theta.setter
    def theta(self, value):
        self._theta = value

    @property
    def posicoesAntigas(self):
        return self._posicoesAntigas.copy()

    def __changePosition(self, target: Ponto):
        # TODO: Magic number
        if len(self._posicoesAntigas) >= 5:
            self._posicoesAntigas.pop(0)
        self._posicoesAntigas.append(Ponto(self._ponto.x, self._ponto.y))
        # ?????
        c = Campo()
        c.release(c.transform2Grid(self.posicao))

    def predicaoAdaptativa(self):
        pass

    def __str__(self):
        return 'Agente\nPosição: ' + str(self.posicao) + '\nTheta: ' + str(self.theta) + '\nPosicoes antigas: ' + str(self.posicoesAntigas)
