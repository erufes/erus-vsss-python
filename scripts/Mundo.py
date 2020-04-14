""" Nome do módulo :        Mundo
    Ano de criação :        2019/10
    Descrição do módulo :   Módulo que define o Mundo onde ocorre o jogo
    Versão :                2.0
    Pré-requisitos :        Padrão Singleton
                            Jogador
                            Ball
                            ComportamentosJogadores Comportamentos
    Membros :               Lorena Bassani
"""
from Patterns.Singleton import Singleton
from Geometria import Ponto
# from Jogador import Jogador
# from ComportamentosJogadores.Comportamentos import COMPORTAMENTOS
# from ControlePartida import Partida, ControladorTime
from Ball import Ball
from Campo import Campo
from enum import Enum
# import math as m


class Lado(Enum):
    ESQUERDO = 0
    DIREITO = 1


class ArenaVSSSDK(object):
    cantoSuperior = {"Direito": Ponto(170, 0),
                     "Esquerdo": Ponto(0, 0)
                     }
    cantoInferior = {"Direito": Ponto(170, 130),
                     "Esquerdo": Ponto(0, 130)
                     }
    golDireito = {"Superior": Ponto(160, 45),
                  "Meio": Ponto(160, 65),
                  "Inferior": Ponto(160, 95)
                  }
    golEsquerdo = {"Superior": Ponto(10, 45),
                   "Meio": Ponto(10, 65),
                   "Inferior": Ponto(10, 95)
                   }
    marcacoes = {"Meio": Ponto(85, 65)
                 }
    metricas = {"Tamanho ": (170, 130),
                "Gol": (10, 40)
                }

    def __init__(self, campo=Campo(celulasX=15, celulasY=13), alliesSide=Lado.ESQUERDO):
        self.campo = campo
        self.alliesSide = alliesSide


class Mundo(Singleton):

    def __init__(self, arena=None, allies=list(), enemies=list()):
        self.__jogadores = {"allies": list(), "enemies": list()}
        self.ball: Ball = Ball()
        self.arena = arena

    """ Nome da função :     inimigos (getter)
        Intenção da função : Retorna os Inimigos
        Pré-requisitos :     Nenhum
        Efeitos colaterais : Nenhum
        Parâmetros :         Nenhum
        Retorno :            list<Inimigos> : Lista de Inimigos
    """
    @property
    def inimigos(self):
        return self.__jogadores["enemies"]

    # Comentários em bloco por algum motivo quebram a definição do setter ali embaixo
    #    Nome da função :     inimigos (setter)
    #    Intenção da função : Alterar a lista de inimigos
    #    Pré-requisitos :     Nenhum
    #    Efeitos colaterais : Altera todo o time de inimigos
    #    Parâmetros :         Novo time de Inimigos
    #    Retorno :            Nenhum
    #

    @inimigos.setter
    def inimigos(self, inimigos):
        self.__jogadores["enemies"].clear()
        self.__jogadores["enemies"].extend(inimigos)

    @property
    def time(self):
        return self.__jogadores["allies"]

    @time.setter
    def time(self, newTime):
        self.__jogadores["allies"].clear()
        self.__jogadores["allies"].extend(newTime)

    def control(self):
        pass

    def __defineFunction(self):
        pass

    def __str__(self):
        out_string = ''
        out_string += '[Modelo de Mundo]\n'
        out_string += 'Possui %d aliados registrados:\n %s\n' % (len(self.__jogadores['allies']), str(self.__jogadores['allies']))
        out_string += 'Possui %d inimigos registrados:\n %s\n' % (len(self.__jogadores['enemies']), str(self.__jogadores['enemies']))
        return out_string
