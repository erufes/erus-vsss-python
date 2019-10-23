""" Nome do módulo :        ComportamentoLissajous
    Ano de criação :        2019/10
    Descrição do módulo :   Modela um comportamento que descreve uma curva de Lissajous
    Versão :                1.0
    Pré-requisitos :        IComportamento
                            Geometria
                            math
    Membros :               Lorena B Bassani
"""
from .IComportamento import IComportamento
from ..Geometria import Ponto
from ..Mundo import Mundo, Arena, Lado
from ..Jogador import Jogador
from ..Ball import Ball
import math as m

class ComportamentoLissajous(IComportamento):
    __PI = 3.14159
    def __init__(self, A = 30, B = 100, a = 3, b = 4, sig = (ComportamentoLissajous.__PI/2)):
        IComportamento.__init__(self)
        self.A = A
        self.B = B
        self.a = a
        self.b = b
        self.sigma = sig
        self.__t = 0
    
    def definirObjetivo(self, jogador, Mundo):
        """ Na matemática, a curva de Lissajous (figura de Lissajous ou curva de Bowditch) 
            é o gráfico produzido por um sistema de equações paramétricas que descreve um complexo movimento harmônico.
            x = A*sen(at + sig), y = B*sen(bt)
        """
        x = self.A*m.sin(self.a*self.__t + self.sigma)
        y = self.B*m.sin(self.b*self.__t)
        self.__t += 1
        return Ponto(x, y)