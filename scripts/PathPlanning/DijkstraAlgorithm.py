""" Nome do módulo :        DijkstraAlgorithm
    Ano de criação :        2019/10
    Descrição do módulo :   Algoritmo de Dijkstra para busca de caminho em grafos
    Versão :                1.0
    Pré-requisitos :        IPathPlanning
                            WeightedGridGraph
                            PriorityQueue
    Membros :               Lorena Bassani
"""
from .Graph import WeightedGridGraph
from .IPathPlanning import IPathPlanning
from queue import PriorityQueue

""" Instead of exploring all possible paths equally, it favors lower cost paths.
    We can assign lower costs to encourage moving on roads, higher costs to avoid
    forests, higher costs to discourage going near enemies, and more. When movement
    costs vary, we use this instead of Breadth First Search.
"""
class DijkstraAlgorithm(IPathPlanning):

    @staticmethod
    def PathPlan(graph, start, goal):
        frontier = PriorityQueue()
        frontier.put((0, start))
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            _, current = frontier.get()
            if current == goal:
                break
            neighbors = graph.neighbors(current)
            for prox, occ in neighbors:
                new_cost = cost_so_far[current] + graph.cost(current, prox)
                if occ is None and (prox not in cost_so_far or new_cost < cost_so_far[prox]):
                    cost_so_far[prox] = new_cost
                    priority = new_cost
                    frontier.put((priority, prox))
                    came_from[prox] = current
        return came_from, cost_so_far