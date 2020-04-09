""" Nome do módulo :      Agente
    Ano de criação :      2019/10
    Descrição do módulo : Agente representa uma entidade em campo
    Versão :              2.0
    Pré-requisitos :      sklearn
                          geometria
    Membros :             Lorena Bassani
"""
# from sklearn.linear_model import LinearRegression

from .Geometria import Ponto
from .Campo import Campo
import math as m

class Agente(object):

    def __init__(self, ponto = Ponto()):
        self.__ponto = ponto
        self.__theta = 0
        self.__posicoesAntigas = list()

    @property
    def ponto(self):
        return self.__ponto

    @ponto.setter
    def ponto(self, value):
        self.__changePosition()
        self.__ponto = value
        c = Campo()
        c.occupy(c.transform2Grid((value.x, value.y)), self)

    @property
    def posicao(self):
        return self.ponto.posicao

    @posicao.setter
    def posicao(self, value):
        self.__changePosition()
        self.ponto.posicao = value
        c = Campo()
        c.occupy(c.transform2Grid(value), self)

    @property
    def x(self):
        return self.ponto.x

    @property
    def y(self):
        return self.ponto.y

    @property
    def theta(self):
        return self.__theta

    @theta.setter
    def theta(self, value):
        self.__theta = value

    @property
    def posicoesAntigas(self):
        return self.__posicoesAntigas.copy()

    def __changePosition(self):
        if len(self.__posicoesAntigas) >= 5:
            self.__posicoesAntigas.pop(0)
        self.__posicoesAntigas.append(Ponto(self.ponto.x, self.ponto.y))
        c = Campo()
        c.release(c.transform2Grid(self.posicao))

    def predicaoAdaptativa(self):
        pass