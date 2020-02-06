from .Player import Player
from .World import *
import numpy as np
from .lista_marcacoes import *
'''posicaox = [0,0,0,0] para pegar o vetor velocidade
posicaoy = [0,0,0,0]'''

class Goalkeeper(Player):
    def __init__(self):
        Player.__init__(self)

    def defende(self, world):

        xp, yp = world.get_ball().predict_ball_method(self, world)

        posx = world.get_team_goal()[0] + 10

        theta_r = math.atan2(float(yp - world.trave_left_upper[1]),
                             float(xp - (world.trave_left_upper[0])))
        theta_s = math.atan2(float(yp - world.trave_left_lower[1]),
                             float(xp - (world.trave_left_lower[0])))

        m_bissetriz = math.tan((theta_r + theta_s) / 2.0)

        bissetriz = -m_bissetriz * (xp - posx) + yp

        posy = (bissetriz*3 + yp) /4.0

        if(abs(posx - world.get_ball().getx()) < 30):
            posy = yp
        if posy < world.trave_left_upper[1] - 1.8:
            posy = world.trave_left_upper[1] - 1.8
            posx -= 3
        if posy > world.trave_left_lower[1] + 1.8:
            posx -= 3
            posy = world.trave_left_lower[1] + 1.8

        adiciona_ponto(int(world.trave_left_upper[0]), int(world.trave_left_upper[1]),255,255,2555,'xg+20, yg')
        adiciona_ponto(int(world.trave_left_lower[0]), int(world.trave_left_lower[1]),255,255,2555,'xg+20, yg')

        return posx , posy # coordenadas que o goleiro deve ficar

    def controle(self, world):
        pd = self
        xfront , yfront = pd.get_front()  #unidade das coordenadas eh cm
        xback , yback = pd.get_back()  #unidade das coordenadas eh cm
        pd_x , pd_y = pd.getx() , pd.gety()  #unidade das coordenadas eh cm
        xb, yb = self.defende(world) # coordenadas que o goleiro deve ficar

        theta_jog = self.get_theta()
        theta_ball = math.atan2(yb,xb) # unidade rad
       
        # matriz de rotacao e matriz de translacao que colocar o eixo de coordanadas no robo alinhado com o theta, e calcula o angulo de erro        
        M_rot = np.array([[math.cos(theta_jog), math.sin(theta_jog)], [-math.sin(theta_jog), math.cos(theta_jog)]])
        M_trans =  np.array([[pd_x], [pd_y]])
        oldcoords_bola = np.array([[xb], [yb]])
        newcoords_bola = M_rot.dot(oldcoords_bola - M_trans)

        # erro robo bola baseado 
        theta_erro = math.atan2(newcoords_bola[1][0], newcoords_bola[0][0])

        #distancia das rodas em metros
        D = 0.075 

        #tempo de amostragem
        T = 30

        #dado o sistema y = pseudoA*Matriz_erro obtem-se y que eh a velocidade da roda direita e velocidade da roda esquerda
        A = np.array([[math.cos(theta_jog)/2, math.cos(theta_jog)/2], [math.sin(theta_jog)/2, math.sin(theta_jog)/2],[1/D, -1/D]])
        pseudoA = np.linalg.pinv(A)
        Matriz_erro = (T)*np.array([[(xb - pd_x)/100], [(yb - pd_y)/100], [theta_erro]])
        y = pseudoA.dot(Matriz_erro)
        vmax = max(abs(y[0][0]), abs(y[1][0])) # paga a maior velocidade

        #como a velocidade foi parametrizada pela maior, K eh a maior velocidade que a roda pode assumir
        K = 200
        vr, vl = y[0][0]*K/vmax, y[1][0]*K/vmax  #mudei a constante para 255 antes era 100
      
        return int(vr), int(vl)