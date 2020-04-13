""" Nome do módulo :        ComportamentoAtacante
    Ano de criação :        2019/10
    Descrição do módulo :   Comportamento de Atacante para Jogadores
    Versão :                1.0
    Pré-requisitos :        IComportamento
                            Geometria
                            Mundo, Arena, Lado
                            Jogador
                            Ball
                            math
    Membros :               Lorena Bassani
"""
from .IComportamento import IComportamento
from ..Geometria import Ponto
from ..Mundo import Mundo, ArenaVSSSDK, Lado
from ..Jogador import Jogador
# from ..Ball import Ball
# import math as m


class ComportamentoAtacante(IComportamento):
    def __init__(self):
        IComportamento.__init__(self)

    def definirObjetivo(self, jogador: Jogador, mundo: Mundo):
        ball = mundo.ball
        if ball.ponto.distancia(jogador.ponto) > 30:
            x, y = ball.posicao
            # Se posicionar antes da bola
            if mundo.lado == Lado.DIREITO:
                x += 3.35
            else:
                x -= 3.35
            # Se a bola estiver acima do meio de campo, se posicionar acima dela
            if y < ArenaVSSSDK.marcacoes["Meio"].y:
                y -= 3.35
            else:
                y += 3.35
            return Ponto(x, y)
        elif ball.ponto.distancia(jogador.ponto) > 5:
            return ball.ponto
        else:
            resp = ArenaVSSSDK.golEsquerdo["Meio"] if mundo.lado == Lado.ESQUERDO else ArenaVSSSDK.golDireito["Meio"]
            return resp
