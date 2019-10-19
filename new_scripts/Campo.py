""" Nome do módulo :        Campo
    Ano de criação :        2019/10
    Descrição do módulo :   Modelar o campo do jogo
    Versão :                1.0
    Pré-requisitos :        WeightedGridGraph
                            Pattern.Singleton
    Membros :               Lorena B Bassani
"""
from .Patterns.Singleton import Singleton
from .PathPlanning.Graph import WeightedGridGraph

class Campo(Singleton, WeightedGridGraph):
    def __init__(self, celulasX : int, celulasY : int, dimX = 150, dimY = 130):
        Singleton.__init__(self)
        WeightedGridGraph.__init__(self, celulasX, celulasY)
        self.__h = (dimX/(celulasX - 1), dimY/(celulasY - 1))

    @property
    def tamanhoCelula(self):
        return self.__h

    def transform2Cart(self, cel):
        # TODO : Ver Se as grades possuem as mesmas características de crescimento de coordenadas
        i, j = WeightedGridGraph.transform2Cart(self, cel)
        return (i*self.__h[0], j*self.__h[1])

    def transform2Grid(self, cel):
        # TODO : Redefinir trasnformação
        pass