""" Nome do módulo :        Campo
    Ano de criação :        2019/10
    Descrição do módulo :   Modelar o campo do jogo
    Versão :                1.0
    Pré-requisitos :        WeightedGridGraph
                            Pattern.Singleton
    Membros :               Lorena B Bassani
"""
from Patterns.Singleton import Singleton
from PathPlanning.Graph import WeightedGridGraph


class Campo(WeightedGridGraph, Singleton):

    def __init__(self, celulasX: int, celulasY: int, dimX: int = 150, dimY: int = 130):
        # ??????
        if not hasattr(self, "grade"):
            WeightedGridGraph.__init__(self, celulasX, celulasY)
            self.__h = (dimX / (celulasX - 1), dimY / (celulasY - 1))

    @property
    def tamanhoCelula(self):
        return self.__h

    def transform2Cart(self, cel):
        # TODO : Ver Se as grades possuem as mesmas características de crescimento de coordenadas
        i, j = WeightedGridGraph.transform2Cart(self, cel)
        return (i * self.__h[0], j * self.__h[1])

    def transform2Grid(self, cel):
        # TODO : Redefinir trasnformação
        x, y = cel
        return WeightedGridGraph.transform2Grid(self, (x // self.__h[0], y // self.__h[1]))

    def cost(self, start, goal):
        # TODO : Redefinir custo para variar com a proximidade a um obstáculo
        return WeightedGridGraph.cost(self, start, goal)

    # def __str__(self):
    #     out_string = '[Campo]'
    #     out_string = 'Possui dimensões: %d x %d' % ()
    #     return '[Campo]'
