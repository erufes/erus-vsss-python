""" Nome do módulo :        AStar
    Ano de criação :        2019/10
    Descrição do módulo :   Algoritmo A* para Planejameto de Trajetória
    Versão :                1.0
    Pré-requisitos :        IPathPlanning
                            WeightedGridGraph
                            PriorityQueue
    Membros :               Lorena Bassani
"""
from .IPathPlanning import IPathPlanning
from .Graph import WeightedGridGraph
from queue import PriorityQueue

""" A* is a modification of Dijkstra’s Algorithm that is optimized for 
    a single destination. Dijkstra’s Algorithm can find paths to all 
    locations; A* finds paths to one location, or the closest of several 
    locations. It prioritizes paths that seem to be leading closer to a goal.
"""
class AStar(IPathPlanning):

    @staticmethod
    def PathPlan(graph, start, goal):
        # FIXME : Está percorrendo todo o mapa, não apenas na direção do objetivo
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()            
            if current == goal:
                break
            neighbors = graph.neighbors(current)
            for prox, occ in neighbors:
                new_cost = cost_so_far[current] + graph.cost(current, prox)
                if occ is None and (prox not in cost_so_far or new_cost < cost_so_far[prox]):
                    cost_so_far[prox] = new_cost
                    priority = new_cost + AStar.__heuristic(graph.transform2Cart(goal), graph.transform2Cart(prox))
                    frontier.put(prox, priority)
                    came_from[prox] = current

        return came_from, cost_so_far

    @staticmethod
    def __heuristic(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)