""" Nome do módulo :        IPathPlanning
    Ano de criação :        2019/10
    Descrição do módulo :   Interface de Algoritmos de Planejamento de Trajetória
    Versão :                1.0
    Pré-requisitos :
    Membros :               Lorena Bassani
"""

class IPathPlanning(object):

    @staticmethod
    def PathPlan(graph, start, goal):
        raise NotImplementedError

    @staticmethod
    def reconstructPath(cameFrom, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = cameFrom[current]
        path.append(start) # optional
        path.reverse() # optional
        return path