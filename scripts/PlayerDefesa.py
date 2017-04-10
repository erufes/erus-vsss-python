import Player
import math
import World
import numpy as np
from lista_marcacoes import *

class PlayerDefesa(Player.Player):

    def chuta(self, world):

        distancia_pra_sair_da_parede = 3.5

        ball = world.get_ball()
        xb,yb = ball.getx(),ball.gety()
        xb, yb = ball.predict_ball_method(self)
        xg, yg = world.get_enemy_goal()

        vec_to_ball_x = xb - self.getx()
        vec_to_ball_y = yb - self.gety()

        norm_vec_to_ball = math.sqrt(vec_to_ball_x**2 + vec_to_ball_y **2)

        vec_to_goal_x = xg - xb
        vec_to_goal_y = yg - yb

        norm_vec_to_goal = math.sqrt(vec_to_goal_x**2 + vec_to_goal_y **2)

        vec_to_goal_x /= norm_vec_to_goal
        vec_to_goal_y /= norm_vec_to_goal

        a,b = int(xb - 0.35 * norm_vec_to_ball*vec_to_goal_x), int (yb - 0.35 *norm_vec_to_ball * vec_to_goal_y)

        """
        if b > world.FIELD_BOTTOM - 12:
            b = world.FIELD_BOTTOM + 24
        elif b < world.FIELD_TOP + 12:
            b = world.FIELD_TOP - 24
        if a > world.FIELD_RIGHT -12:
            a = world.FIELD_RIGHT - 24
        elif a < world.FIELD_LEFT + 12:
            a = world.FIELD_LEFT + 24
        """
        """
        if b > world.FIELD_BOTTOM:
            b = world.FIELD_BOTTOM - 3
        elif b < world.FIELD_TOP:
            b = world.FIELD_TOP + 3
        if a > world.FIELD_RIGHT - 4:
            a = world.FIELD_RIGHT - 8
        elif a < world.FIELD_LEFT + 4:
            a = world.FIELD_LEFT + 8"""


        return xb,yb


        p = world.get_goalkeeper()
        x,y = p.getx(),p.gety()

        theta_robo = self.get_theta()
        distance_to_amiguinho = math.sqrt((x-self.getx())**2 + (y-self.gety())**2)
        if distance_to_amiguinho < 15.0 and self.gety() > y:
            x,y = self.getx() , self.gety()+20
            return x , y
        elif distance_to_amiguinho < 15.0 and self.gety() < y:
            x,y = self.getx() , self.gety()-20
            return x , y

        if self.getx() > world.FIELD_RIGHT and xb < self.getx():
            return self.getx() - 30, self.gety()

        if yb > world.FIELD_BOTTOM - distancia_pra_sair_da_parede or yb < world.FIELD_TOP + distancia_pra_sair_da_parede or xb > world.FIELD_RIGHT -distancia_pra_sair_da_parede or xb < world.FIELD_LEFT + distancia_pra_sair_da_parede:
            #print "aqui"         
            if self.gety() > world.FIELD_BOTTOM - distancia_pra_sair_da_parede and (theta_robo > 30 and theta_robo < 150) :
                return self.getx(),self.gety() -15
            elif self.gety() < world.FIELD_TOP + distancia_pra_sair_da_parede and (theta_robo > -150 and theta_robo < 30):
                return self.getx(),self.gety() +15
            if self.getx() > world.FIELD_RIGHT -distancia_pra_sair_da_parede:
                a = world.FIELD_RIGHT - 15
                return a,b
            elif self.getx() < world.FIELD_LEFT + distancia_pra_sair_da_parede:
                a = world.FIELD_LEFT + 15
                return a,b

            return xb, yb

        if self.gety() > world.FIELD_BOTTOM - distancia_pra_sair_da_parede and (theta_robo > 30 and theta_robo < 150):
            b = world.FIELD_BOTTOM - 15
            a = self.getx()
            return a,b
        elif self.gety() < world.FIELD_TOP + distancia_pra_sair_da_parede and (theta_robo > -150 and theta_robo < 30):
            b = world.FIELD_TOP + 15
            a = self.getx()
            return a,b
        if self.getx() > world.FIELD_RIGHT -distancia_pra_sair_da_parede:
            a = world.FIELD_RIGHT - 15
            b = self.gety()
            return a,b
        elif self.getx() < world.FIELD_LEFT + distancia_pra_sair_da_parede:
            a = world.FIELD_LEFT + 15
            b = self.gety()
            return a,b


        #p = world.get_def_player()


        distance_to_ball = math.sqrt((xb-self.getx())**2 + (yb-self.gety())**2)
        ###########################################################################
        if distance_to_ball < 20 and xb > self.getx(): #chuta a bola pro campo inimigo
            return (xb + 2*(xb-self.getx())), (yb + 2*(yb - self.gety()))
        if(not(yb+ (yb - self.gety()) > yg +20 or (yb+ (yb - self.gety()) < yg-20)) and xb < self.getx()): # caso esteja na do gol dar a volta
            if(yb < yg + 20 and yb < self.gety()): # dando a volta por cima (bjs recalque)
                if(b+20 > world.FIELD_BOTTOM):
                    if(a -5 < world.FIELD_LEFT +15):
                        return world.FIELD_LEFT +20 , world.FIELD_BOTTOM -15
                    else:
                        return a-5 , world.FIELD_BOTTOM -15
                if(b+20 < world.FIELD_TOP):
                    if(a -5 < world.FIELD_LEFT +15):
                        return world.FIELD_LEFT +20 , world.FIELD_BOTTOM +15
                    else:
                        return a-5 , world.FIELD_BOTTOM +15
                else:
                    if(a -5 < world.FIELD_LEFT +15):
                        return world.FIELD_LEFT +20 , b+20
                    else:
                        return a-5 , b+20
            else: # dando a volta por baixo
                if(b-20 > world.FIELD_BOTTOM):
                    if(a -5 < world.FIELD_LEFT +15):
                        return world.FIELD_LEFT +20 , world.FIELD_BOTTOM -15
                    else:
                        return a-5 , world.FIELD_BOTTOM -15
                if(b-20 < world.FIELD_TOP):
                    if(a -5 < world.FIELD_LEFT +15):
                        return world.FIELD_LEFT +20 , world.FIELD_BOTTOM +15
                    else:
                        return a-5 , world.FIELD_BOTTOM +15
                else:
                    if(a -5 < world.FIELD_LEFT +15):
                        return world.FIELD_LEFT +20 , b-20
                    else:
                        return a-5 , b-20
        if(a -5 < world.FIELD_LEFT +15):
            return world.FIELD_LEFT +20 , b
        else:
            return a,b


    def controle(self, world):

    	pd = world.get_def_player()
        xfront , yfront = pd.get_front()  #unidade das coordenadas eh cm
        xback , yback = pd.get_back()  #unidade das coordenadas eh cm
       	pd_x , pd_y = pd.getx() , pd.gety()  #unidade das coordenadas eh cm
        xb, yb = world.get_ball().getxy() #unidade das coordenadas eh cm
        #xb, yb = self.chuta();
    
        theta_jog = self.get_theta()
        theta_ball = math.atan2(yb,xb) # unidade rad
        theta_gol = math.atan2(236,515)

       
        # matriz de rotacao e matriz de translacao que colocar o eixo de coordanadas no robo alinhado com o theta, e calcula o angulo de erro        
        M_rot = np.array([[math.cos(theta_jog), math.sin(theta_jog)], [-math.sin(theta_jog), math.cos(theta_jog)]])
        M_trans =  np.array([[pd_x], [pd_y]])
        oldcoords_bola = np.array([[xb], [yb]])
        newcoords_bola = M_rot.dot(oldcoords_bola - M_trans)

        oldcoords_gol = np.array([515,236])
        newcoords_gol = M_rot.dot(oldcoords_gol - M_trans)

        # erro robo bola baseado 
        #theta_erro = math.atan2(newcoords_bola[1][0], newcoords_bola[0][0])
        theta_erro_bola = math.atan2(newcoords_bola[1][0], newcoords_bola[0][0])
        theta_erro_gol = math.atan2(newcoords_gol[1][0], newcoords_gol[0][0])

        theta_erro = theta_erro_bola + (theta_erro_bola - theta_erro_gol)/3
       
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
        K = 150
    	vr, vl = y[0][0]*K/vmax, y[1][0]*K/vmax  #mudei a constante para 255 antes era 100

        return int(vr), int(vl)