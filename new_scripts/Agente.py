""" Nome do módulo :      Agente
    Ano de criação :      2019/10
    Descrição do módulo : Agente representa uma entidade em campo
    Versão :              2.0
    Pré-requisitos :      sklearn
                          geometria
    Membros :             Lorena Bassani
"""
from sklearn.linear_model import LinearRegression
from .Geometria import Ponto

class Agente(object):

    def __init__(self, ponto = Ponto()):
        self.__ponto = ponto
        self.__posicoesAntigas = list()
    
    @property
    def ponto(self):
        return self.__ponto
    
    @ponto.setter
    def ponto(self, value):
        self._changePosition()
        self.__ponto = value
    
    @property
    def posicao(self):
        return self.ponto.posicao
    
    @posicao.setter
    def posicao(self, value):
        self._changePosition()
        self.ponto.posicao = value
    
    @property
    def x(self):
        return self.ponto.x
    
    @property
    def posicoesAntigas(self):
        return self.__posicoesAntigas.copy()
    
    def _changePosition(self):
        if(len(self.__posicoesAntigas) >= 5):
            self.__posicoesAntigas.pop(0)
        self.__posicoesAntigas.append(Ponto(self.ponto.x, self.ponto.y))

    def predicaoAdaptativa(self):
        pass