""" VSSS-o-Primeiro
    Nome do módulo :        simulador
    Ano de criação :        2021/07
    Descrição do módulo:    Modulo para rodar o simulador no código do VSSS (terceira versão)
    Versão:                 3.0
    Pré-requisitos :        Simulação do Webots para vsss da ERUS (https://github.com/erufes/v4s-webots)
    Membros:                Lorena Bassani
"""

import requests

from old_scripts.World import World
from old_scripts.PlayerAtaque import PlayerAtaque
from old_scripts.PlayerDefesa import PlayerDefesa
from old_scripts.Goalkeeper import Goalkeeper

ports = {
    'Blue'   : [40001, 40002, 40003],
    'Yellow' : [30001, 30002, 30003]
}

local = 'http://localhost'

controle_simulador = "4002"

def main():
    world_blue = World()

    world_blue.add_atk_player( PlayerAtaque() )
    world_blue.add_def_player( PlayerDefesa() )
    world_blue.add_gk_player( Goalkeeper() )

    world_yellow = World()
    world_yellow.goal = 1

    world_yellow.add_atk_player( PlayerAtaque() )
    world_yellow.add_def_player( PlayerDefesa() )
    world_yellow.add_gk_player( Goalkeeper() )

    # inicia o jogo
    url_controle = local + ":" + str(controle_simulador)
    request = {
        'method' : 'start_sim',
        'jsonrpc' : '2.0',
        'id'      : 0
    }
    requests.post(url_controle, json=request)

    while True:
        mensagens = dict()
        
        # Atualização da bola e do mundo
        request = {
            'method' : 'get_state',
            'jsonrpc' : '2.0',
            'id'      : 0
        }
        response = requests.post(url_controle, json=request).json()['result'] # requisição de estado do jogo para o simulador
        
        # Posições da bola
        pos_ball_x = response['ball']['position'][0]
        pos_ball_y = response['ball']['position'][1]

        # Atualização e ação do Time Azul
        p0_x = response['Blue'][0]['position'][0]
        p0_y = response['Blue'][0]['position'][1]
        p0_theta = response['Blue'][0]['rotation'][3]

        p1_x = response['Blue'][1]['position'][0]
        p1_y = response['Blue'][1]['position'][1]
        p1_theta = response['Blue'][1]['rotation'][3]

        p2_x = response['Blue'][2]['position'][0]
        p2_y = response['Blue'][2]['position'][1]
        p2_theta = response['Blue'][2]['rotation'][3]
        
        world_blue.update(p0_x, p0_y, p0_theta, p1_x, p1_y, p1_theta, p2_x, p2_y, p2_theta, (pos_ball_x, pos_ball_y))

        mensagens['Blue'] = list()
        for i in range(0,3):
            p = world_blue.get_teammate(i)
            vr, vl = p.controle(world_blue)
            vr = remap(vr, -255, 255, 0, 10)
            vl = remap(vl, -255, 255, 0, 10)
            mensagens['Blue'].append({
                    'method'  : 'move',
                    'params'  : [vr, vl],
                    'jsonrpc' : '2.0',
                    'id'      : 0
                })

        # Atualização e ação do Time Amarelo
        p0_x = response['Yellow'][0]['position'][0]
        p0_y = response['Yellow'][0]['position'][1]
        p0_theta = response['Yellow'][0]['rotation'][3]

        p1_x = response['Yellow'][1]['position'][0]
        p1_y = response['Yellow'][1]['position'][1]
        p1_theta = response['Yellow'][1]['rotation'][3]

        p2_x = response['Yellow'][2]['position'][0]
        p2_y = response['Yellow'][2]['position'][1]
        p2_theta = response['Yellow'][2]['rotation'][3]
        
        world_yellow.update(p0_x, p0_y, p0_theta, p1_x, p1_y, p1_theta, p2_x, p2_y, p2_theta, (pos_ball_x, pos_ball_y))
        mensagens['Yellow'] = list()
        for i in range(0,3):
            p = world_yellow.get_teammate(i)
            vr, vl = p.controle(world_yellow)
            vr = remap(vr, -255, 255, 0, 10)
            vl = remap(vl, -255, 255, 0, 10)
            mensagens['Yellow'].append({
                    'method'  : 'move',
                    'params'  : [vr, vl],
                    'jsonrpc' : '2.0',
                    'id'      : 0
                })

        # envio das mensagens
        for team in ports.keys():
            for i in range(0,3):
                url = local + ":" + str(ports[team][i])
                requests.post(url, json=mensagens[team][i])
            

def remap( x, oMin, oMax, nMin, nMax ):

    #range check
    if oMin == oMax:
        print ("Warning: Zero input range")
        return None

    if nMin == nMax:
        print ("Warning: Zero output range")
        return None

    #check reversed input range
    reverseInput = False
    oldMin = min( oMin, oMax )
    oldMax = max( oMin, oMax )
    if not oldMin == oMin:
        reverseInput = True

    #check reversed output range
    reverseOutput = False   
    newMin = min( nMin, nMax )
    newMax = max( nMin, nMax )
    if not newMin == nMin :
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result

if __name__ == '__main__':
    main()
