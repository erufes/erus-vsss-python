""" Nome do módulo :        Graph
    Ano de criação :        2019/10
    Descrição do módulo :   Implementa SimpleGraph e GridGaph
    Versão :                1.0
    Pré-requisitos :        Nenhum
    Membros :               Lorena Bassani
"""
from typing import Tuple, Dict

# TODO: Revisar os comentários de tipagem desse arquivo


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

    def __str__(self):
        return '[SimpleGraph]\n' + str(self.edges)


class GridGraph(object):
    def __init__(self, dim_x: int, dim_y: int) -> None:
        self._sizex: int = dim_x
        self._sizey: int = dim_y
        self._dimensions: Dict[str, int] = {'x': dim_x, 'y': dim_y}
        self._data: Dict = dict()
        self._maxSize = dim_x * dim_y

    """ Nome da função :     grid (getter)
        Intenção da função : Retorna as dimensões da Grade
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         Nenhum
        Retorno :            (nx, ny) : Dimensão da Grade
    """
    @property
    def dimensions(self) -> Dict:
        return self._dimensions

    """ Nome da função :     occupy
        Intenção da função : Ocupar uma celula com um objeto
        Pré-requisitos :     Celula pertencente a Grade
        Efeitos colaterais : A Celula informada passa a ser ocupada pelo objeto
        Parâmetros :         Tuple(int, int) : Celula a ser ocupada
                             object          : Objeto que irá ocupar a célula
        Retorno :            Nenhum
    """
    def occupy(self, cel: Tuple[int, int], obj) -> None:
        if not self.is_inside_grid(cel):
            raise IndexError('Célula inexistente')
        # Check if _data already has an object inside
        if cel in self._data:
            self._data[cel].append(obj[1])
        else:
            self._data[cel] = [obj]

    """ Nome da função :     release
        Intenção da função : Libera a Celula
        Pré-requisitos :     Celula pertencente a Grade e ocupada
        Efeitos colaterais : Desocupa a celula (Cuidado, pode eliminar se for a única referência para ele)
        Parâmetros :         int : Celula a ser liberada
        Retorno :            Nenhum
    """

    def release(self, cel: Tuple[int, int]) -> None:
        if self.get_occuppier(cel) is not None:
            del self._data[cel]

    """ Nome da função :     is_occupied
        Intenção da função : Dizer se a celula está ocupada
        Pré-requisitos :     Celula pertencente a Grade
        Efeitos colaterais : Nenhum
        Parâmetros :         int : Celula que se deseja saber se está ocupada
        Retorno :            Boolean : True se estiver ocupada, False caso contrário
    """

    def is_occupied(self, cel: Tuple[int, int]) -> bool:
        return self.get_occuppier(cel) is not None

    """ Nome da função :     get_occuppier
        Intenção da função : Retornar referência ao objeto que ocupa uma celula, junto com a celula ocupada
        Pré-requisitos :     Celula pertecente a Grade
        Efeitos colaterais : Nenhum
        Parâmetros :         int : Celula a ser retornada
        Retorno :            (int, object) : Celula e objeto que a ocupa (None se não for ocupada)
    """

    def get_occuppier(self, cel: Tuple[int, int]) -> list:
        if cel in self._data:
            return self._data[cel]
        return []

    """ Nome da função :     is_inside_grid
        Intenção da função : Dizer se uma celula está na Grade
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         int : Celula que se deseja saber se pertence a Grade
        Retorno :            Boolean : True se pertencer a grade, False caso contrário
    """

    def is_inside_grid(self, cel: Tuple[int, int]) -> bool:
        return 0 <= cel[0] * cel[1] < self._maxSize

    """ Nome da função :     whatis_occupied
        Intenção da função : Retornar todos os pontos ocupados da Grade
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         Nenhum
        Retorno :            list : Lista de Celulas ocupadas na Grade
    """

    def whatis_occupied(self):
        lst = [k for k in self._data]
        return lst

    """ Nome da função :     neighbors
        Intenção da função : Retornar Vizinhos da Celula
        Pré-requisitos :     Celula pertencente a Grade
        Efeitos colaterais : Nenhum
        Parâmetros :         int : Celula que se deseja saber os vizinhos
        Retorno :            list : Lista com as celulas vizinhas
    """

    def neighbors(self, cel: Tuple[int, int]) -> list:
        nbs = []
        cels = []
        idx = self.transform2grid(cel)
        cels.append(idx - self._dimensions['x'])
        cels.append(idx + self._dimensions['x'])
        if idx % self._dimensions['x'] > 0:
            cels.append(idx - 1)
        if idx % self._dimensions['x'] < self._dimensions['x'] - 1:
            cels.append(idx + 1)
        for c in cels:
            conv = self.transform2cart(c)
            if self.is_inside_grid(conv):
                nbs.append(conv)
        return nbs

    """ Nome da função :     transform2cart
        Intenção da função : Transforma uma celula da Grade em um ponto cartesiano correspondente
        Pré-requisitos :     Celula pertencente a Grade
        Efeitos colaterais : Nenhum
        Parâmetros :         int : Celula que se deseja saber as coordenadas cartesianas
        Retorno :            (int, int) : Coordenadas cartesianas correrpondestes a celula
    """

    def transform2cart(self, cel: int) -> Tuple[int, int]:
        return cel % self._dimensions['x'], cel // self._dimensions['y']

    """ Nome da função :     transform2grid
        Intenção da função : Transformar um ponto cartesiano em um ponto da grade
        Pré-requisitos :     Ponto pertencente ao dominio [0, 0]x[nx, ny]
        Efeitos colaterais : Nenhum
        Parâmetros :         (int, int) : Coordenadas cartesianas do ponto que se deseja saber a celula na Grade
        Retorno :            int : Celula correspondente ao ponto
    """

    def transform2grid(self, cel: Tuple[int, int]) -> int:
        x, y = cel
        return y * self._dimensions['x'] + x

    def __str__(self):
        out_str = '[Grid Graph]\n'
        out_str += 'Dimensões: %d x %d\n' % (self._sizex, self._sizey)
        out_str += 'Conteúdo: \n'
        out_str += str(self._data)
        return out_str


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
        raise NotImplementedError
        return 1

    # def __str__(self):
    #     out_str = '[Weighted Grid Graph]\n'
    #     # out_str += 'Dimensões do grafo: %d x %d' % (celulasX, celulasY)
    #     return out_str
