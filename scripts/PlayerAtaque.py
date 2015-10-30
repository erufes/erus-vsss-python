import Player
import math
import World
from lista_marcacoes import *

class PlayerAtaque(Player.Player):



    def chuta(self, world):

        distancia_pra_sair_da_parede = 3.5

        ball = world.get_ball()
        xb,yb = ball.getx(),ball.gety()
        xb, yb = ball.predict_ball_method_ofensive(self)
        xg, yg = world.get_enemy_goal()

        adiciona_ponto(int(xb), int(yb), 127, 255, 60, 'bola')

        vec_to_ball_x = xb - self.getx()
        vec_to_ball_y = yb - self.gety()

        norm_vec_to_ball = math.sqrt(vec_to_ball_x**2 + vec_to_ball_y **2)

        vec_to_goal_x = xg - xb
        vec_to_goal_y = yg - yb

        norm_vec_to_goal = math.sqrt(vec_to_goal_x**2 + vec_to_goal_y **2)

        vec_to_goal_x /= norm_vec_to_goal
        vec_to_goal_y /= norm_vec_to_goal
        a,b = int(xb - 0.35 * norm_vec_to_ball*vec_to_goal_x), int (yb - 0.35 *norm_vec_to_ball * vec_to_goal_y)

        adiciona_ponto(int(xg), int(yg+20),255,255,2555,'xg+20, yg')
        adiciona_ponto(int(xg), int(yg-20),255,255,2555,'xg-20, yg')
        theta_robo = self.get_theta()
        #print theta_robo
        
        if self.getx() > world.FIELD_RIGHT and xb < self.getx():
            return self.getx() - 30, self.gety()

        if yb > world.FIELD_BOTTOM - distancia_pra_sair_da_parede or yb < world.FIELD_TOP + distancia_pra_sair_da_parede or xb > world.FIELD_RIGHT -distancia_pra_sair_da_parede or xb < world.FIELD_LEFT + distancia_pra_sair_da_parede:
            #print "aqui"         
            if self.gety() > world.FIELD_BOTTOM - distancia_pra_sair_da_parede and (theta_robo > 30 and theta_robo < 150) :
                return self.getx(),self.gety() -15
            elif self.gety() < world.FIELD_TOP + distancia_pra_sair_da_parede and (theta_robo > -150 and theta_robo < 30):
                return self.getx(),self.gety() +15
            if self.getx() > world.FIELD_RIGHT -distancia_pra_sair_da_parede +1 and (yb > yg-20 and yb < yg+20):
                a = world.FIELD_RIGHT - 15
                return a,b
            if self.getx() < world.FIELD_LEFT + distancia_pra_sair_da_parede:
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
        #if self.getx() > world.FIELD_RIGHT -distancia_pra_sair_da_parede:
            #a = world.FIELD_RIGHT - 15
            #b = self.gety()
            #return a,b
        if self.getx() < world.FIELD_LEFT + distancia_pra_sair_da_parede:
            a = world.FIELD_LEFT + 15
            b = self.gety()
            return a,b

        #a = a -5

        p = world.get_def_player()
        x,y = p.getx(),p.gety()

        adiciona_ponto(int(xg), int(yg+20),255,255,2555,'xg+20, yg')
        adiciona_ponto(int(xg), int(yg-20),255,255,2555,'xg-20, yg')
        distance_to_amiguinho = math.sqrt((x-self.getx())**2 + (y-self.gety())**2)

        if distance_to_amiguinho < 20:
            x,y = self.getx()+5,self.gety() 
            return int(x),int(y)

        #return a,b
#        Quando o jogador se aproxima muito da bola, o setpoint deve ficar atras da bola, garantindo que ele chute a bola

        distance_to_ball = math.sqrt((xb-self.getx())**2 + (yb-self.gety())**2)
        if distance_to_ball < 15 and xb > self.getx():
            if(not(yb+ (yb - self.gety()) > yg + 20 or (yb+ (yb - self.gety()) < yg-20))): # so alterar o setpoint caso ajude a fazer gol.
                return (xb + 1*(xb-self.getx())), (yb+ 1*(yb - self.gety()))
            if(self.getx() - xg and self.gety() - yb): # faz gol na diagonal (sqn)
                if(yb > self.gety() and self.gety() < yg-20):#parte de cima do campo
                    if(math.atan2(self.gety() - (yg-20),(self.getx()-xg)) - math.atan2(self.gety() -(yg+20),(self.getx()-xg)) > math.atan2((self.getx() - xb),(self.gety() - yb))):
                        return (xb + 1*(xb-self.getx())), (yb+ 1*(yb - self.gety()))
                if(yb < self.gety() and self.gety() > yg+20 ):#parte de baixo do campo
                    if(math.atan2(self.gety() - (yg+20),(self.getx()-xg)) - math.atan2(self.gety() -(yg-20),(self.getx()-xg)) > math.atan2((self.getx() - xb),(self.gety() - yb))):
                        return (xb + 1*(xb-self.getx())), (yb+ 1*(yb - self.gety()))
            #if(yb < yg -20 and yb < self.gety()):
                #return a , b-15
            #if(yb > yg +20 and yb > self.gety()):
                #return a, b+15
        return a, b

        """cm = (self.getx() + 5) 
        raio = ((self.getx() - xb)**2 + (self.gety() - yb)**2)/2
        x_x0 = cm - (self.getx() + xb)/2
        y0 = (self.gety() + yb)/2
        c = x_x0**2 + y0**2-raio
        if(yb < self.gety()):
            y_final = y0 + (abs(y0**2 - c))**0.5
        else:
            y_final = y0 - (abs(y0**2 - c))**0.5"""
        #return a, b
        '''cm = math.pi/6
        raio = ((abs((self.getx() - xb)**2 + (self.gety() - yb)**2))**0.5)/2
        #if(not(self.gety() > yb)):
        #y_final = (self.gety() + yb)/2 + raio*math.sin(math.pi)
        #x_final = (self.getx() + xb)/2 + raio*math.cos(math.pi) 
        #else:
        if(self.gety() > yb):
            teta = -math.atan2((xb - self.getx()),yb - self.gety()) -cm # roda pra cima
        else:
            teta = math.pi/2 +math.atan2((xb - self.getx()),yb - self.gety()) 

        y_final = (self.gety() + yb)/2 + raio*math.sin(teta)
        x_final = (self.getx() + xb)/2 + raio*math.cos(teta) 
        if(xb < self.getx()):# and xb > (world.FIELD_RIGHT + world.FIELD_LEFT)/2.0  ):
            if(y_final > world.FIELD_BOTTOM):
                return x_final , world.FIELD_BOTTOM -7
            if(y_final < world.FIELD_TOP):
                return x_final , world.FIELD_BOTTOM +7
            else:
                return x_final , y_final
        elif(self.getx() < xb and yb > self.gety() and yb > yg+20):
            teta = math.pi/2 +math.atan2((xb - self.getx()),yb - self.gety()) 
            #teta = -math.atan2((xb - self.getx()),yb - self.gety()) -cm # roda pra cima
            y_final = (self.gety() + yb)/2 + raio*math.sin(teta)
            x_final = (self.getx() + xb)/2 + raio*math.cos(teta)
            if(y_final > world.FIELD_BOTTOM):
                return x_final , world.FIELD_BOTTOM -7
            if(y_final < world.FIELD_TOP):
                return x_final , world.FIELD_BOTTOM +7
            else:
                return x_final , y_final
        elif(self.getx() < xb and yb < self.gety() and yb < yg -20 ):
            teta = -math.atan2((xb - self.getx()),yb - self.gety()) -cm # roda pra cima
            y_final = (self.gety() + yb)/2 + raio*math.sin(teta)
            x_final = (self.getx() + xb)/2 + raio*math.cos(teta)
            if(y_final > world.FIELD_BOTTOM):
                return x_final , world.FIELD_BOTTOM -7
            if(y_final < world.FIELD_TOP):
                return x_final , world.FIELD_BOTTOM +7
            else:
                return x_final , y_final'''    
        return a , b


    def controle(self, world):
        
        # TODO: habilitar o setpoint depois
        (xt, yt) = self.chuta(world)
        if world.get_ball().getx() < (world.FIELD_RIGHT + world.FIELD_LEFT)/2.0:
            xt = ((world.FIELD_RIGHT + world.FIELD_LEFT)/2.0)+15
            yt = world.FIELD_TOP + 50
        
        adiciona_ponto(int(xt), int(yt), 0,255,255, 'xt, yt')

        #xt = yt = 100; 

        distancia_y = int(yt) - self.gety()
        distancia_x = int(xt) - self.getx()

        theta_alvo = math.atan2(distancia_y, distancia_x )
        theta_alvo *= 180.0/3.1415#conversao p/ graus

        theta_robo = self.get_theta()
        #print "orientacao do robo = ", theta_robo

        theta_erro = theta_alvo - theta_robo
        
        
        while theta_erro > 180.0:
            theta_erro -= 360.0
        while theta_erro < -180.0:
            theta_erro += 360.0
        
        ro = math.sqrt(distancia_y*distancia_y + distancia_x*distancia_x)

        alfa = theta_erro *math.pi/180.0 #conversao para radianos

        # if (ro < 8) and (xt < (world.FIELD_RIGHT + world.FIELD_LEFT)/2.0):
        #     theta_erro = 90 - self.get_theta()
        #
        #     while theta_erro > 180.0:
        #         theta_erro -= 360.0
        #     while theta_erro < -180.0:
        #         theta_erro += 360.0
        #
        #     alfa = theta_erro * math.pi / 180.0
        #     return self.lyapunov(ro, alfa, 0, 80.0, 45.0)

        # ni eh a velocidade de avanco do modelo d Lyapunov
        # alphaomega eh a voelocidade de giro

        k_alfa_omega = 150.0
        k_ni = 216.0
        fator_freio = 156 # fator_freio = 8/(tanh^(-1)(13/255)) para obter pwm = 13 com ro = 8!

        #print "---------"
        #print "ro = ", ro

        #print "alfa_graus = ", 180*alfa/math.pi

        # vr, vl = self.lyapunov(ro, alfa, 200.0, 50.0, 15.0) #k_ni,k_alphaomega,fator_freio
        vr, vl = self.lyapunov(ro, alfa, 240.0, 20.0, 12.0)
        #vr, vl = self.lyapunov(ro, alfa, 255.0, 50.0, 15.0) #k_ni,k_alphaomega,fator_freio
        
        #melhor ate agora para atacante vr, vl = self.lyapunov(ro, alfa, 240.0, 25.0, 12.0)

        #vr, vl =  self.lyapunov(ro, alfa, k_ni, k_alfa_omega, fator_freio) #k_ni,k_alphaomega,fator_freio
        return vr, vl