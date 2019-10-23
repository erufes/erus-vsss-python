""" VSSS-o-Primeiro
    Nome do módulo :        simulador
    Ano de criação :        2019/10  
    Descrição do módulo:    Modulo para rodar o simulador no código do VSSS (segunda versão)
    Versão:                 2.0
    Pré-requisitos :        vsscorepy
    Membros:                Lorena Bassani
    
"""
from vsscorepy.communications.command_sender import CommandSender
from vsscorepy.communications.debug_sender import DebugSender
from vsscorepy.communications.state_receiver import StateReceiver
from vsscorepy.domain.command import Command
from vsscorepy.domain.wheels_command import WheelsCommand
from vsscorepy.domain.point import Point
from vsscorepy.domain.pose import Pose
from vsscorepy.domain.debug import Debug

from new_scripts.Mundo import Mundo
from new_scripts.Inimigo import Inimigo
from new_scripts.Aliado import Aliado
from new_scripts.ComportamentosJogadores.Factory import COMPORTAMENTOS

from enum import Enum
import math as m

class Team(Enum):
    BLUE = 1
    YELLOW = 1

class kernel():

    def __init__(self, team = Team.YELLOW):
        self.state_receiver = StateReceiver()
        self.state_receiver.create_socket()
        self.command_sender = CommandSender()
        self.command_sender.create_socket()
        """ self.debug_sender = DebugSender()
        self.debug_sender.create_socket() """
    
    def envia_comando(self, comando_Player1, comando_Player2, comando_Player3):
        command = Command()
        command.wheels_commands.append(comando_Player1)
        command.wheels_commands.append(comando_Player2)
        command.wheels_commands.append(comando_Player3)
        self.command_sender.send_command(command)
    
    def recebe_estado(self):
        state = self.state_receiver.receive_state()
        return state


k = kernel()
mundo = Mundo()
time = [Aliado(0, comportamento = COMPORTAMENTOS.GOLEIRO), Aliado(1, comportamento = COMPORTAMENTOS.ATACANTE), Aliado(2)]
inimigo = [Inimigo(3), Inimigo(4), Inimigo(5)]
mundo.inimigos = inimigo
mundo.time = time
while True:
    state = k.recebe_estado()
    mundo.ball.posicao = (state.ball.x, state.ball.y)
    mundo.ball.theta = m.atan2(state.ball.speed_y, state.ball.speed_x)
    for i in range(0, len(time)):
        r = state.team_yellow[i]
        e = state.team_blue[i]
        time[i].posicao = (r.x, r.y)
        time[i].theta = r.angle
        inimigo[i].posicao = (e.x, e.y)
        inimigo[i].theta = (e.angle)
    listaComando = mundo.control()
    listaComando = list(map(lambda vel: WheelsCommand(vel[0], vel[1]), listaComando))
    k.envia_comando(listaComando[0], listaComando[1], listaComando[2])    
