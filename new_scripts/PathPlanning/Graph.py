class SimpleGraph(object):
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]

class GridGraph(object):
    def __init__(self, celulasX, celulasY):
        self.__grade = (celulasX, celulasY)
        self.__occupied = list()
    
    @property
    def grid(self):
        return self.__grade
    
    def occupy(self, cel, obj):
        self.__occupied.append((cel, obj))
    
    def release(self, cel):
        liberar = self.getOccupier(cel)
        if liberar:
            self.__occupied.remove(liberar[0])

    def isOccupied(self, cel):
        return self.getOccupier(cel) is not None
    
    def getOccupier(self, cel):
        ocupador = list(filter(lambda x: x[0] == cel, self.__occupied))
        if ocupador:
            return ocupador[0]
        return None