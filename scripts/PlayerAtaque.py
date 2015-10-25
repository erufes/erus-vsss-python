import Player
import math
import World
from lista_marcacoes import *

class PlayerAtaque(Player.Player):



    def chuta(self, world):
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

        adiciona_ponto(int(xg), int(yg+20),255,255,2555,'xg+20, yg')
        adiciona_ponto(int(xg), int(yg-20),255,255,2555,'xg-20, yg')
        if self.getx() > world.FIELD_RIGHT and xb < self.getx():
            return self.getx() - 30, self.gety()

        if b > world.FIELD_BOTTOM - 4.2 or b < world.FIELD_TOP + 4.2 or a > world.FIELD_RIGHT -4.2 or a < world.FIELD_LEFT + 4.2:
            return xb, yb
        a = a -15
        # if b > world.FIELD_BOTTOM - 4.2:
        #     b = world.FIELD_BOTTOM - 8.4
        # elif b < world.FIELD_TOP + 4.2:
        #     b = world.FIELD_TOP + 8.4
        # if a > world.FIELD_RIGHT -4.2:
        #     a = world.FIELD_RIGHT - 8.4
        # elif a < world.FIELD_LEFT + 4.2:
        #     a = world.FIELD_LEFT + 8.4

        p = world.get_def_player()
        x,y = p.getx(),p.gety()

        adiciona_ponto(int(xg), int(yg+20),255,255,2555,'xg+20, yg')
        adiciona_ponto(int(xg), int(yg-20),255,255,2555,'xg-20, yg')
        distance_to_amiguinho = math.sqrt((x-self.getx())**2 + (y-self.gety())**2)

        if distance_to_amiguinho < 20:
            x,y = x+5,y 
            return int(x),int(y)


#        Quando o jogador se aproxima muito da bola, o setpoint deve ficar atras da bola, garantindo que ele chute a bola

        distance_to_ball = math.sqrt((xb-self.getx())**2 + (yb-self.gety())**2)
        if distance_to_ball < 30 and xb > self.getx():
            if(not(yb+ (yb - self.gety()) > yg + 20 or (yb+ (yb - self.gety()) < yg-20))): # so alterar o setpoint caso ajude a fazer gol.
                return (xb + 2*(xb-self.getx())), (yb+ 2*(yb - self.gety()))
            if(self.getx() - xg and self.gety() - yb): # faz gol na diagonal (sqn)
                if(yb > self.gety() and self.gety() < yg-20):#parte de cima do campo
                    if(math.atan2(self.gety() - (yg-20),(self.getx()-xg)) - math.atan2(self.gety() -(yg+20),(self.getx()-xg)) > math.atan2((self.getx() - xb),(self.gety() - yb))):
                        return (xb + 2*(xb-self.getx())), (yb+ 2*(yb - self.gety()))
                if(yb < self.gety() and self.gety() > yg+20 ):#parte de baixo do campo
                    if(math.atan2(self.gety() - (yg+20),(self.getx()-xg)) - math.atan2(self.gety() -(yg-20),(self.getx()-xg)) > math.atan2((self.getx() - xb),(self.gety() - yb))):
                        return (xb + 2*(xb-self.getx())), (yb+ 2*(yb - self.gety()))
            #if(yb < yg -20 and yb < self.gety()):
                #return a , b-15
            #if(yb > yg +20 and yb > self.gety()):
                #return a, b+15

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
        cm = math.pi/6
        raio = ((abs((self.getx() - xb)**2 + (self.gety() - yb)**2))**0.5)/2
        #if(not(self.gety() > yb)):
        #y_final = (self.gety() + yb)/2 + raio*math.sin(math.pi)
        #x_final = (self.getx() + xb)/2 + raio*math.cos(math.pi) 
        #else:
        if(self.gety() > yb):
            teta = -math.atan2((xb - self.getx()),yb - self.gety()) -cm
        else:
            teta = math.pi/2 +math.atan2((xb - self.getx()),yb - self.gety()) 

        y_final = (self.gety() + yb)/2 + raio*math.sin(teta)
        x_final = (self.getx() + xb)/2 + raio*math.cos(teta) 
        if(xb < self.getx() and xb > (world.FIELD_RIGHT + world.FIELD_LEFT)/2.0  ):
            return int(x_final) , int(y_final)
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
        vr, vl = self.lyapunov(ro, alfa, 240.0, 30.0, 17.0)
        #vr, vl = self.lyapunov(ro, alfa, 255.0, 50.0, 15.0) #k_ni,k_alphaomega,fator_freio
        
        #vr, vl =  self.lyapunov(ro, alfa, k_ni, k_alfa_omega, fator_freio) #k_ni,k_alphaomega,fator_freio
        return vr, vl