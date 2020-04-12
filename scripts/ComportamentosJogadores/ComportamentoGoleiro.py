""" Nome do módulo :        ComportamentoGoleiro
    Ano de criação :        2019/10
    Descrição do módulo :   Comportamento de Goleiro para Jogadores
    Versão :                2.0
    Pré-requisitos :        IComportamento
                            Geometria
                            Mundo, Arena, Lado
                            Ball
                            Jogador
                            math
    Membros :               Lorena Bassani
"""
from .IComportamento import IComportamento
from ..Geometria import Ponto
from ..Mundo import Mundo, Arena, Lado
# from ..Ball import Ball
from ..Jogador import Jogador
import math as m


class ComportamentoGoleiro(IComportamento):
    def __init__(self):
        IComportamento.__init__(self)

    def definirObjetivo(self, jogador: Jogador, mundo: Mundo):
        """ Ideia da implementação :
                        Posicionar o robô de forma que ele impessa a trajetória da bola
                                Como : Calcular o angulo de abertura entre a bola e o gol
                                                Posicionar o robô onde o "triangulo" tenha base de 7,5 (tamanho do robô)
                """
        resp = Ponto()
        ball = mundo.ball
        bx, _ = ball.posicao
        bt = ball.theta
        """ a² = b² + c² - 2bc*cos α
            a² - b² - c² = -2bc* cos α
            (b² + c² - a²)/2bc = cos α
            α = acos(((b² + c² - a²)/2bc))
                Onde :
                    a <- lado oposto (tamanho do gol)
                    b e c <- lados adjascentes (distancia da bola até um dos limites do gol)
                    α <- angulo desejado
        """
        gol = Arena.golDireito if mundo.lado == Lado.DIREITO else Arena.golEsquerdo
        a = Arena.metricas["Gol"][1]
        b = ball.ponto.distancia(gol["Superior"])
        c = ball.ponto.distancia(gol["Inferior"])
        alpha = (b ** 2 + c ** 2 - a ** 2) / 2 * b * c
        if alpha > 1:
            alpha = 1.0
        elif alpha < -1:
            alpha = -1.0
        alpha = m.acos(alpha)

        # 3.75 é metade da largura do robô de 7.5x7.5
        dx = 3.75 / m.tan(alpha) if m.tan(alpha) != 0 else 0
        resp.x = bx + dx if mundo.lado == Lado.DIREITO else bx - dx

        theta = m.fabs(bt - jogador.theta)
        resp.y = (resp.x / m.tan(theta))

        resp.y = 100 if resp.y > 100 else 30 if resp.y < 30 else resp.y
        resp.posicao = (10, 65) if mundo.lado == Lado.ESQUERDO and resp.x > 37.5 else (
            150, 65) if mundo.lado == Lado.DIREITO and resp.x < 112.5 else resp.posicao

        return resp
