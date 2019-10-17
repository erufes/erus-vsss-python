""" Nome do módulo :        DijkstraAlgorithm
    Ano de criação :        2019/10
    Descrição do módulo :   Algoritmo de Dijkstra para busca de caminho em grafos
    Versão :                1.0
    Pré-requisitos :        IPathPlanning
    Membros :               Lorena Bassani
"""

from .IPathPlanning import IPathPlanning

""" Instead of exploring all possible paths equally, it favors lower cost paths. 
    We can assign lower costs to encourage moving on roads, higher costs to avoid 
    forests, higher costs to discourage going near enemies, and more. When movement 
    costs vary, we use this instead of Breadth First Search.
"""
class DijkstraAlgorithm(IPathPlanning):

    @staticmethod
    def PathPlan(graph, start, goal):
        pass