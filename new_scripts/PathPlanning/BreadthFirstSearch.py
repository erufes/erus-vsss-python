""" Nome do módulo :        BreadthFirstSearch
    Ano de criação :        2019/10
    Descrição do módulo :   Algoritmo de Busca Primeiro em Largura para Grafos
    Versão :                1.0
    Pré-requisitos :        IPathPlanning
                            GridGraph
                            Queue
    Membros :               Lorena Basasani
"""
from .IPathPlanning import IPathPlanning
from .Graph import GridGraph
from queue import Queue

""" Explores equally in all directions. This is an incredibly useful algorithm, 
    not only for regular path finding, but also for procedural map generation, 
    flow field pathfinding, distance maps, and other types of map analysis. 
"""
class BreadthFirstSearch(IPathPlanning):

    @staticmethod
    def PathPlan(graph, start, goal):
        frontier = Queue()
        frontier.put(start)
        came_from = {}
        came_from[start] = None
        while not frontier.empty():
            current = frontier.get()
            if current == goal:
                break

            for prox in graph.neighbors(current):
                if prox not in came_from and prox[1] == None:
                    frontier.put(prox[0])
                    came_from[prox[0]] = current
        
        return came_from