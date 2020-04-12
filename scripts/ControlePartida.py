from Patterns.Singleton import Singleton
# from Geometria import Ponto
# from Jogador import Jogador
from ComportamentosJogadores.Comportamentos import COMPORTAMENTOS
from enum import Enum


class EstadosPartida(Enum):
    PARADO = 0
    EMANDAMENTO = 1
    PENALTI_NOSSO = 2
    PENALTI_INIMIGO = 3
    ENCERRADA = 4


class PartidaEncerradaException(Exception):
    pass


class Partida(Singleton):

    def __init__(self, *args, **keyargs):
        pass

    def inicializa(self):
        self.__gols = {"HomeTeam": list(), "Enemies": list()}
        self.__estadoPartida = EstadosPartida.PARADO

    def comecaPartida(self):
        if self.estadoPartida == EstadosPartida.ENCERRADA:
            raise PartidaEncerradaException
        else:
            self.estadoPartida = EstadosPartida.EMANDAMENTO

    def marcarGol(self, time, tempo):
        self.__gols[time].append(tempo)

    @property
    def estadoPartida(self):
        return self.__estadoPartida

    @estadoPartida.setter
    def estadoPartida(self, estado):
        self.__estadoPartida = estado

    def calculaEstadoAtual(self):
        pass


class ControladorTime(Singleton):
    def __init__(self, *args, **keyargs):
        pass

    def inicializa(self, team=list()):
        self.__jogadores = team

    def substituicao(self, idPlayerIn, idPlayerOut):
        pass

        """ Nome da função :     goleiro (getter)
        Intenção da função : Retorna o Jogador Goleiro
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         Nenhum
        Retorno :            Aliado : Jogador com Comportamento Goleiro
    """
    @property
    def goleiro(self):
        g = list(filter(lambda x: x.comportamento == COMPORTAMENTOS.GOLEIRO, self.__jogadores))
        if g:
            return g[0]
        return None

    """ Nome da função :     goleiro (setter)
        Intenção da função : Alterar o Goleiro
        Pré-requisitos :     Não ter um Goleiro previamente
        Efeitos colaterais : Define um novo goleiro
        Parâmetros :         int : Id do Jogador para alterar
        Retorno :            Nenhum
    """
    @goleiro.setter
    def goleiro(self, jogadorId):
        if not self.goleiro:
            p = self.jogador(jogadorId)
            p.comportamento = COMPORTAMENTOS.GOLEIRO

    """ Nome da função :     jogador (getter)
        Intenção da função : Retornar um Jogador de Acordo com seu Id
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         int : Id do Jogador
        Retorno :            Jogador : Jogador correspondente ao Id
    """

    def jogador(self, jogadorId):
        p = list(filter(lambda x: x.id == jogadorId, self.__jogadores))
        if p:
            return p
        return None
