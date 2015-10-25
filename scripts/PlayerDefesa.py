import Player
import math
import World
from lista_marcacoes import *

class PlayerDefesa(Player.Player):

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

        if b > world.FIELD_BOTTOM:
            b = world.FIELD_BOTTOM - 3
        elif b < world.FIELD_TOP:
            b = world.FIELD_TOP + 3
        if a > world.FIELD_RIGHT - 4:
            a = world.FIELD_RIGHT - 8
        elif a < world.FIELD_LEFT + 4:
            a = world.FIELD_LEFT + 8

        #p = world.get_def_player()
        p = world.get_atk_player()
        x,y = p.getx(),p.gety()

        distance_to_amiguinho = math.sqrt((x-a)**2 + (y-b)**2)
        if distance_to_amiguinho < 25:
             x,y = x,y+ 15
             return int(x),int(y)
        distance_to_ball = math.sqrt((xb-self.getx())**2 + (yb-self.gety())**2)
        ###########################################################################
        if distance_to_ball < 20 and xb > self.getx(): #chuta a bola pro campo inimigo
            return (xb + 2*(xb-self.getx())), (yb + 2*(yb - self.gety()))
        if(not(yb+ (yb - self.gety()) > yg +20 or (yb+ (yb - self.gety()) < yg-20)) and xb < self.getx()): # caso esteja na do gol dar a volta
            if(yb < yg + 20 and yb < self.gety()): # dando a volta por cima (bjs recalque)
                return a-5 , b+20
            else: # dando a volta por baixo
                return a-5 , b-20
        return a,b


    def controle(self, world):
        
        (xt, yt) = self.chuta(world)
        if xt > (world.FIELD_RIGHT + world.FIELD_LEFT)/2.0:
            xt = (world.FIELD_RIGHT + world.FIELD_LEFT)/2.0
            """if math.sqrt((self.gety()-world.get_ball().gety())**2 + (self.getx()-world.get_ball().getx())**2) < 30: #Se tiver perto roda e da um chutasso, eu acho: revisado por guilherme e paulucio
                if world.get_ball().gety() > self.gety():
                    return 255, -255
                else:
                    return -255, 255"""

        xb, yb = world.get_ball().getxy()
        dx = xb - world.left_goal[0]
        dy = yb - world.left_goal[1]
        ro = math.sqrt(dx**2+dy**2)
        if ro < 30: #se a bola esta dentro da area
            xt, yt = (world.FIELD_LEFT+world.FIELD_RIGHT)*0.5, (world.FIELD_TOP + world.FIELD_BOTTOM) * 0.5

        adiciona_ponto(int(xt), int(yt), 255,0,255, 'xt, yt')

        distancia_y = int(yt) - self.gety()
        distancia_x = int(xt) - self.getx()

        theta_ball = math.atan2(distancia_y, distancia_x )
        theta_ball *= 180.0/3.1415#conversao p/ graus

        theta_pink = self.get_theta()

        theta_erro = theta_ball - theta_pink
        #print theta_pink
        
        while theta_erro > 180.0:
            theta_erro -= 360.0
        while theta_erro < -180.0:
            theta_erro += 360.0
        
        
        ro = math.sqrt(distancia_y*distancia_y + distancia_x*distancia_x)
        if ro == 0:
            ro = 1.0
        alfa = theta_erro *math.pi/180.0 #conversao para radianos

        # ni eh a velocidade de avanco do modelo d Lyapunov

        #print "---------"
        #print "ro = ", ro

        #print "alfa_graus = ", 180*alfa/math.pi

        vr, vl = self.lyapunov(ro, alfa, 230.0, 40.0, 12.0)
        #vr, vl = self.lyapunov(ro, alfa, 110.0, 140.0, 30.0) #original
        #print "vr , vl", vr , vl
        return vr, vl
        
        #return 0,0

# class PlayerDefesa(Player.Player):
#
#     def chuta(self, world):
#         ball = world.get_ball()
#         xb, yb = ball.getx(),ball.gety() #ball.predict_ball_method(self)
#         xg, yg = world.get_enemy_goal()
#
#         vec_to_ball_x = xb - self.getx()
#         vec_to_ball_y = yb - self.gety()
#
#         norm_vec_to_ball = math.sqrt(vec_to_ball_x**2 + vec_to_ball_y **2)
#
#         vec_to_goal_x = xg - xb
#         vec_to_goal_y = yg - yb
#
#         norm_vec_to_goal = math.sqrt(vec_to_goal_x**2 + vec_to_goal_y **2)
#
#         vec_to_goal_x /= norm_vec_to_goal
#         vec_to_goal_y /= norm_vec_to_goal
#
#         return int(xb - 0.35 * norm_vec_to_ball*vec_to_goal_x), int (yb - 0.35 *norm_vec_to_ball * vec_to_goal_y)
#
#     def controle(self, world):
#         (xt, yt) = self.chuta(world)
#         if xt > (world.FIELD_RIGHT + world.FIELD_LEFT)/2.0-30:
#             xt = (world.FIELD_RIGHT + world.FIELD_LEFT)/2.0-30
#             if math.sqrt((self.gety()-world.get_ball().gety())**2 + (self.getx()-world.get_ball().getx())**2) < 25:
#                 if world.get_ball().gety() > self.gety():
#                     return 255, -255
#                 else:
#                     return -255, 255
#
#         xb, yb = world.get_ball().getxy()
#         dx = xb - world.left_goal[0]
#         dy = yb - world.left_goal[1]
#         ro = math.sqrt(dx**2+dy**2)
#         if ro < 50: #se a bola esta dentro da area
#             xt, yt = world.FIELD_LEFT + 50, world.FIELD_TOP + 50
#
#         distancia_y = int(yt) - self.gety()
#         distancia_x = int(xt) - self.getx()
#
#         theta_ball = math.atan2(distancia_y, distancia_x )
#         theta_ball *= 180.0/3.1415#conversao p/ graus
#
#         theta_pink = self.get_theta()
#
#         theta_erro = theta_ball - theta_pink
#
#         while theta_erro > 180.0:
#             theta_erro -= 360.0
#         while theta_erro < -180.0:
#             theta_erro += 360.0
#
#         ro = math.sqrt(distancia_y*distancia_y + distancia_x*distancia_x)
#         if ro == 0:
#             ro = 1.0
#         alfa = theta_erro *math.pi/180.0 #conversao para radianos
#
#         # ni eh a velocidade de avanco do modelo d Lyapunov
#
#         return self.lyapunov(ro, alfa, 90.0, 110.0, 40.0)