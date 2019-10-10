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
from vsscorepy.communications.command_sender import CommandSender
from vsscorepy.communications.debug_sender import DebugSender
from vsscorepy.communications.state_receiver import StateReceiver
from vsscorepy.domain.command import Command
from vsscorepy.domain.wheels_command import WheelsCommand
from vsscorepy.domain.point import Point
from vsscorepy.domain.pose import Pose
from vsscorepy.domain.debug import Debug
from enum import Enum

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
        self.team = team
    
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
while True:
    state = k.recebe_estado()
    vel1 = 10
    vel2 = -10
    comando = WheelsCommand(vel1, vel2)
    k.envia_comando(comando, comando, comando)
    