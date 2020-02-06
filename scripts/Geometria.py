""" Nome do módulo :      Geometria
    Ano de criação :      2019/10 
    Descrição do módulo : Módulo de auxílio para calculos geometricos
    Versão :              1.0
    Pré-requisitos :      math
    Membros :             Lorena Bassani
"""
import math as m

class Ponto(object):

    """ Nome da função :     Ponto (Construtor)
        Intenção da função : Iniciar objeto tipo Ponto
        Pré-requisitos :     Nenhum
        Efeitos colaterais : As coordenadas do ponto serão setadas para os valores passados
                             como parametro ou (0, 0) caso não seja especificado na chamada.
        Parâmetros :         float : Coordenada x
                             float : Coordenada y
        Retorno :            Objeto tipo ponto criado
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    """ Nome da função :     Getters e Setters
        Intenção da função : Acesso de escrita e leitura as propriedades de Ponto
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Pode alterar propriedades
        Parâmetros :         Variados
        Retorno :            Variados
    """

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
    
    @property
    def posicao(self):
        return (self.x, self.y)
    
    @posicao.setter
    def posicao(self, value):
        x, y = value
        self.x = x
        self.y = y
    
    def __eq__(self, outro):
        return self.posicao == outro.posicao

    """ Nome da função :     distancia
        Intenção da função : Calcular a distância entre dois pontos
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         Ponto : ponto para calcular a distância a partir deste
        Retorno :            float : distância entre os pontos
    """
    def distancia(self, outro):
        return m.sqrt((self.x - outro.x)**2 + (self.y - outro.y)**2)

def to180range(angle):
    M_PI = 3.14159
    angle = m.fmod(angle, 2 * M_PI)
    if (angle < - M_PI):
        angle = angle + 2 * M_PI
    elif (angle > M_PI):
        angle = angle - 2 * M_PI
    return angle