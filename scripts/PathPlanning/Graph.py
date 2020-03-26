""" Nome do módulo :        Graph
    Ano de criação :        2019/10
    Descrição do módulo :   Implementa SimpleGraph e GridGaph
    Versão :                1.0
    Pré-requisitos :        Nenhum
    Membros :               Lorena Bassani
"""
class SimpleGraph(object):
    def __init__(self):
        self.edges = {}

    """ Nome da função :     neighbors
        Intenção da função : Retorna os Vizinhos do nó
        Pré-requisitos :     Nó pertencente ao grafo
        Efeitos colaterais : Nenhum
        Parâmetros :         Nó : Nó do qual se deseja saber os vizinhos
        Retorno :            list : Vizinhos do Nó
    """
    def neighbors(self, id):
        return self.edges[id]

class GridGraph(object):
    def __init__(self, celulasX, celulasY):
        self.__grade = (celulasX, celulasY)
        self.__occupied = list()

    """ Nome da função :     grid (getter)
        Intenção da função : Retorna as dimensões da Grade
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         Nenhum
        Retorno :            (nx, ny) : Dimensão da Grade
    """
    @property
    def grid(self):
        return self.__grade

    """ Nome da função :     occupy
        Intenção da função : Ocupar uma celula com um objeto
        Pré-requisitos :     Celula pertencente a Grade
        Efeitos colaterais : A Celula informada passa a ser ocupada pelo objeto
        Parâmetros :         int : Celula a ser ocupada
                             object : Objeto que irá ocupar a célula
        Retorno :            Nenhum
    """
    def occupy(self, cel, obj):
        if self.isInsideGrid(cel):
            self.__occupied.append((cel, obj))

    """ Nome da função :     release
        Intenção da função : Libera a Celula
        Pré-requisitos :     Celula pertencente a Grade e ocupada
        Efeitos colaterais : Desocupa a celula (Cuidado, pode eliminar se for a única referência para ele)
        Parâmetros :         int : Celula a ser liberada
        Retorno :            Nenhum
    """
    def release(self, cel):
        liberar = self.getOccupier(cel)
        if liberar:
            self.__occupied.remove(liberar)

    """ Nome da função :     isOccupied
        Intenção da função : Dizer se a celula está ocupada
        Pré-requisitos :     Celula pertencente a Grade
        Efeitos colaterais : Nenhum
        Parâmetros :         int : Celula que se deseja saber se está ocupada
        Retorno :            Boolean : True se estiver ocupada, False caso contrário
    """
    def isOccupied(self, cel):
        return self.getOccupier(cel) is not None

    """ Nome da função :     getOccupier
        Intenção da função : Retornar referência ao objeto que ocupa uma celula, junto com a celula ocupada
        Pré-requisitos :     Celula pertecente a Grade
        Efeitos colaterais : Nenhum
        Parâmetros :         int : Celula a ser retornada
        Retorno :            (int, object) : Celula e objeto que a ocupa (None se não for ocupada)
    """
    def getOccupier(self, cel):
        ocupador = list(filter(lambda x: x[0] == cel, self.__occupied))
        if ocupador:
            return ocupador[0]
        return None

    """ Nome da função :     isInsideGrid
        Intenção da função : Dizer se uma celula está na Grade
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         int : Celula que se deseja saber se pertence a Grade
        Retorno :            Boolean : True se pertencer a grade, False caso contrário
    """
    def isInsideGrid(self, cel):
        return cel >= 0 and cel < self.__grade[0]*self.__grade[1]

    """ Nome da função :     whatIsOccupied
        Intenção da função : Retornar todos os pontos ocupados da Grade
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         Nenhum
        Retorno :            list : Lista de Celulas ocupadas na Grade
    """
    def whatIsOccupied(self):
        return list(map(lambda x: x[0], self.__occupied))

    """ Nome da função :     neighbors
        Intenção da função : Retornar Vizinhos da Celula
        Pré-requisitos :     Celula pertencente a Grade
        Efeitos colaterais : Nenhum
        Parâmetros :         int : Celula que se deseja saber os vizinhos
        Retorno :            list : Lista com as celulas vizinhas
    """
    def neighbors(self, cel):
        nbs = list()
        cels = list()
        cels.append(cel - self.__grade[0])
        cels.append(cel + self.__grade[0])
        if cel % self.__grade[0] > 0:
            cels.append(cel - 1)
        if cel % self.__grade[0] < self.__grade[0] - 1:
            cels.append(cel + 1)

        for c in cels:
            if self.isInsideGrid(c):
                o = self.getOccupier(c)
                if o is None:
                    o = (c, None)
                nbs.append(o)
        return nbs

    """ Nome da função :     transform2Cart
        Intenção da função : Transforma uma celula da Grade em um ponto cartesiano correspondente
        Pré-requisitos :     Celula pertencente a Grade
        Efeitos colaterais : Nenhum
        Parâmetros :         int : Celula que se deseja saber as coordenadas cartesianas
        Retorno :            (int, int) : Coordenadas cartesianas correrpondestes a celula
    """
    def transform2Cart(self, cel):
        return (cel % self.__grade[0], cel // self.__grade[0])

    """ Nome da função :     transform2Grid
        Intenção da função : Transformar um ponto cartesiano em um ponto da grade
        Pré-requisitos :     Ponto pertencente ao dominio [0, 0]x[nx, ny]
        Efeitos colaterais : Nenhum
        Parâmetros :         (int, int) : Coordenadas cartesianas do ponto que se deseja saber a celula na Grade
        Retorno :            int : Celula correspondente ao ponto
    """
    def transform2Grid(self, cel):
        x, y = cel
        return y*self.__grade[0] + x

class WeightedGridGraph(GridGraph):
    def __init__(self, celulasX, celulasY):
        GridGraph.__init__(self, celulasX, celulasY)

    """ Nome da função :        cost
        Intenção da função :    Calcula o custo de se mover de start até goal
        Pré-requisitos :        Nenhum
        Efeitos colaterais :    Nenhum
        Parâmetros :            int : Celula de Inicio
                                int : Celula de Objetivo
        Retorno :               int : Custo de movimentação pela grade
    """
    def cost(self, start, goal):
        return 1
