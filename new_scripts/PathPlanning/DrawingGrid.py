""" Nome do módulo :        GraphDrawer
    Ano de criação :        2019/10
    Descrição do módulo :   Desenha o Grafo em tela
    Versão :                1.0
    Pré-requisitos :        GridGraph
    Membros :               Lorena Bassani
"""
from .Graph import GridGraph
class GridDrawer(object):
    @staticmethod
    def draw_tile(graph, c, style, width):
        r = "."
        if 'number' in style and c in style['number']: r = "%d" % style['number'][c]
        if 'point_to' in style and style['point_to'].get(graph.transform2Grid(c), None) is not None:
            (x1, y1) = c
            (x2, y2) = graph.transform2Cart(style['point_to'][graph.transform2Grid(c)])
            if x2 == x1 + 1: r = ">"
            if x2 == x1 - 1: r = "<"
            if y2 == y1 + 1: r = "v"
            if y2 == y1 - 1: r = "^"
        if 'start' in style and c == style['start']: r = "A"
        if 'goal' in style and c == style['goal']: r = "Z"
        if 'path' in style and c in style['path']: r = "@"
        if c in list(map(lambda x : graph.transform2Cart(x), graph.whatIsOccupied())) : r = "#" * width
        return r

    @staticmethod
    def draw_grid(graph, width=2, **style):
        nx, ny = graph.grid
        for y in range(ny):
            for x in range(nx):
                print("%%-%ds" % width % GridDrawer.draw_tile(graph, (x, y), style, width), end="")
            print()
