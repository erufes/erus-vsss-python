""" VSSS-o-Primeiro
    Nome do módulo :        simulador
    Ano de criação :        2019/01  
    Descrição do módulo:    Modulo para rodar o simulador no código do VSSS (primeira versão)
    Versão:                 1.0
    Pré-requisitos :        vsscorepy
    Membros:                Lorena Bassani
    
"""
import vsscorepy as simulador
import scripts as vsss_erus
from scripts.World import World
from scripts.Goalkeeper import Goalkeeper as gk
from scripts.PlayerAtaque import PlayerAtaque as fw
from scripts.PlayerDefesa import PlayerDefesa as df
from scripts.Ball import Ball
from scripts.Player import Player
from scripts.Agent import Agent
from new_scripts.Controle.ControleTrajeto.ControleSiegwart import ControleSiegwart
from vsscorepy.communications.command_sender import CommandSender
from vsscorepy.communications.debug_sender import DebugSender
from vsscorepy.communications.state_receiver import StateReceiver
from vsscorepy.domain.command import Command
from vsscorepy.domain.wheels_command import WheelsCommand
from vsscorepy.domain.point import Point
from vsscorepy.domain.pose import Pose
from vsscorepy.domain.debug import Debug
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
mundo = World()
team = [fw(), df(), gk()]
mundo.add_atk_player(team[0])
mundo.add_def_player(team[1])
mundo.add_gk_player(team[2])
enemie = [Player(), Player(), Player()]
mundo.jogadores["Enemies"].extend(enemie)
controle = ControleSiegwart()
while True:
    state = k.recebe_estado()
    mundo.ball.update_position((state.ball.x, state.ball.y))
    for i in range(0, 2):
        r = state.team_yellow[i]
        e = state.team_blue[i]
        team[i].set_position_xyt(r.x, r.y, r.angle)
        enemie[i].set_position_xyt(e.x, e.y, e.angle)
    
    listaComando = list()
    for p in team:
        ox, oy = p.chuta(mundo)
        objetivo = (ox, oy, m.atan2(oy, ox))
        ax, ay = p.getxy()
        atual = (ax, ay, p.get_theta())
        vell, velr = controle.controle(actualValue = atual, objective = objetivo, speed = 60)
        listaComando.append(WheelsCommand(vell, velr))
    k.envia_comando(listaComando[0], listaComando[1], listaComando[2])