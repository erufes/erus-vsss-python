""" Nome do módulo :        AStar
    Ano de criação :        2019/10
    Descrição do módulo :   Algoritmo A* para Planejameto de Trajetória
    Versão :                1.0
    Pré-requisitos :        IPathPlanning
    Membros :               Lorena Bassani
"""
from .IPathPlanning import IPathPlanning

""" A* is a modification of Dijkstra’s Algorithm that is optimized for 
    a single destination. Dijkstra’s Algorithm can find paths to all 
    locations; A* finds paths to one location, or the closest of several 
    locations. It prioritizes paths that seem to be leading closer to a goal.
"""
class AStar(IPathPlanning):

    @staticmethod
    def PathPlan(graph, start, goal):
        pass

    @staticmethod
    def __heuristic(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)