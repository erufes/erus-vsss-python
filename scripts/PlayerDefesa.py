from .Player import Player
import math
from .World import World
import numpy as np
from .lista_marcacoes import *

class PlayerDefesa(Player):
    def __init__(self):
        Player.__init__(self)

    def chuta(self, world):

        distancia_pra_sair_da_parede = 3.5

        #captura de dados : bola, inimigo
        ball = world.get_ball()					#Pega bola
        xb, yb = ball.predict_ball_method(self, world)	#Pega valor estimado de onde a bola estara
        xgi, ygi = world.get_enemy_goal()		#Pega posicoes x e y do gol do oponente
        xg, yg = world.get_team_goal()			#Pega posicoes x e y do proprio gol
        xd, yd = self.getxy()					#Pega posicoes x e y do jogador defendor

        adiciona_ponto(int(xg), int(yg), 0, 0, 0, 'enemy',int(xg), int(yg)) #laranja : Nao sei o que isso significa :D


        #calculo distancia bola ao defensor : INICIO
        vec_to_ball_x = xb - self.getx()
        vec_to_ball_y = yb - self.gety()
        norm_vec_to_ball = math.sqrt(vec_to_ball_x**2 + vec_to_ball_y **2)
        #calculo distancia bola ao defensor : FIM

        #calculo distancia da bola para o gol Aliado : INICIO
        vec_to_goal_x = xg - xb
        vec_to_goal_y = yg - yb
        norm_vec_to_goal = math.sqrt(vec_to_goal_x**2 + vec_to_goal_y **2)
		#calculo distancia da bola para o gol Aliado : FIM

        vec_to_goal_x /= norm_vec_to_goal#Vetor para o gol Aliado
        vec_to_goal_y /= norm_vec_to_goal#Vetor para o gol Aliado
	
        #Calculo da distancia da defesa para o gol : INICIO
        vec_def_goal_x = xg - xd
        vec_def_goal_y = yg - yd 
        norm_vec_def_goal = math.sqrt(vec_def_goal_x**2 + vec_def_goal_y**2)#distancia da defesa pro gol
        #Calculo da distancia da defesa para o gol : FIM
		
        #para impedir colicoes com o goleiro : INICIO
        p = world.get_goalkeeper()[0]
        x,y = p.getx(),p.gety()
        theta_robo = self.get_theta()

        distance_to_amiguinho = math.sqrt((x-self.getx())**2 + (y-self.gety())**2)
        if distance_to_amiguinho < 15.0 and self.gety() > y:
            x,y = self.getx() , self.gety()+20
            return x , y
        elif distance_to_amiguinho < 15.0 and self.gety() < y:
            x,y = self.getx() , self.gety()-20
            return x , y
		#para impedir colicoes com o goleiro : FIM

        xm = xg - xgi#calculo do meio de campo X
        ym = yg - ygi#calculo do meio de campo Y
		
        #calculo da distancia da bola pro meio : INICIO
        vec_ball_meio_x = xb - xmeioRicardo
        vec_ball_meio_y = yb - ymeioRicardo
        norm_vec_ball_meio = math.sqrt(vec_ball_meio_x**2 + vec_ball_meio_y**2)#distancia da bola pro meio
        #calculo da distancia da bola pro meio : FIM
		##########


        #print 'Bola->Gol ', norm_vec_to_goal, 'Bola->Meio', norm_vec_ball_meio, 'Def->Gol', norm_vec_def_goal
        #Estrategia para tirar a bola de perto do gol : INICIO
        if norm_vec_to_goal < norm_vec_ball_meio:  #norm_vec_to_goal eh a distancia da bola para o gol
            if norm_vec_def_goal < norm_vec_to_goal:
                return xb,yb
            elif yb < 62.5:
                if yd < yb:
                    return xd, yd
                elif yd != yb:
                    return xg , yg - 21
                else:
                    return xd, yd
            else:
                if yd < yb:
                    return xg, yg + 21
                elif yd != yb:
                    return xd, yd
                else:
                    return xd, yd
        else:
            return vec_to_ball_x, vec_to_ball_y
        #Estrategia para tirar a bola de perto do gol : FIM
        
		#Nunca vai pras funcoes abaixo pq n existe a e b que eu nao sei o que eh :( 			(Ricardo)
        #Tem que fazer novo :D (Ricardo) pra sair da parede
        
        #Codigo para sair da parede!! : INICIO
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
        
        #Codigo para sair da parede!! : FIM

    def controle(self, world):

        pd = self
        xfront , yfront = pd.get_front()  		#unidade das coordenadas eh cm
        xback , yback = pd.get_back()  			#unidade das coordenadas eh cm
       	pd_x , pd_y = pd.getx() , pd.gety()  	#unidade das coordenadas eh cm
        xb, yb = world.get_ball().getxy() 		#unidade das coordenadas eh cm // usada para ver se o zagueiro vai direto para a bola
        
        theta_jog = self.get_theta()
        theta_ball = math.atan2(yb,xb) 			# unidade rad
        theta_gol = math.atan2(236,515)

       
        # matriz de rotacao e matriz de translacao que colocar o eixo de coordanadas no robo alinhado com o theta, e calcula o angulo de erro      
        M_rot = np.array([[math.cos(theta_jog), math.sin(theta_jog)], [-math.sin(theta_jog), math.cos(theta_jog)]])
        M_trans =  np.array([[pd_x], [pd_y]])
        oldcoords_bola = np.array([[xb], [yb]])
        newcoords_bola = M_rot.dot(oldcoords_bola - M_trans)

        oldcoords_gol = np.array([515,236])
        newcoords_gol = M_rot.dot(oldcoords_gol - M_trans)

        # erro robo bola baseado 
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
        K = 100
        vr, vl = y[0][0]*K/vmax, y[1][0]*K/vmax  #mudei a constante para 255 antes era 100

        return int(vr), int(vl)