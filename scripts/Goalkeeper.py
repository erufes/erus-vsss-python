import Player
from World import *
from lista_marcacoes import *
'''posicaox = [0,0,0,0] para pegar o vetor velocidade
posicaoy = [0,0,0,0]'''

class Goalkeeper(Player.Player):
    def defende(self, world):

        xp, yp = world.get_ball().predict_ball_method(self)
        #adiciona_ponto(int(xp), int(yp), 255, 0, 102, 'bola prevista')

        posx = world.get_team_goal()[0] + 10

        '''
        theta_r = math.atan2(float(world.get_ball().gety() - world.trave_left_upper[1]),
                             float(world.get_ball().getx() - (world.trave_left_upper[0])))
        theta_s = math.atan2(float(world.get_ball().gety() - world.trave_left_lower[1]),
                             float(world.get_ball().getx() - (world.trave_left_lower[0])))
        '''

        theta_r = math.atan2(float(yp - world.trave_left_upper[1]),
                             float(xp - (world.trave_left_upper[0])))
        theta_s = math.atan2(float(yp - world.trave_left_lower[1]),
                             float(xp - (world.trave_left_lower[0])))

        m_bissetriz = math.tan((theta_r + theta_s) / 2.0)

        #bissetriz = -m_bissetriz * (world.get_ball().getx() - posx) + world.get_ball().gety()
        bissetriz = -m_bissetriz * (xp - posx) + yp

        #posy = (bissetriz + world.get_ball().gety()) * 0.5
        #posy = (bissetriz*3 + world.get_ball().gety()) /4.0
        posy = (bissetriz*3 + yp) /4.0

        if(abs(posx - world.get_ball().getx()) < 30):
            #posy = world.get_ball().gety()
            posy = yp
            #print posy

        if posy < world.trave_left_upper[1] - 1.8:
            posy = world.trave_left_upper[1] - 1.8
            posx -= 3
        if posy > world.trave_left_lower[1] + 1.8:
            posx -= 3
            posy = world.trave_left_lower[1] + 1.8

        # kc = 0.1 #kc define a curvatura do trajeto de setpoint do goleiro
        # posx = world.get_team_goal()[0] - 30 + abs(kc*(posy - world.get_team_goal()[1]))

            # cv2.circle(frame,(   int(posx)   , int(posy)   ),5,(200,100,100),-1)
            
        '''
        posicaox[1] = posicaox[0] #guarda posicao antiga da bolinha
        posicaox[0] = world.get_ball().getx() #atualiza posicao atual da bolinha

        posicaoy[1] = posicaoy[0]
        posicaoy[0] = world.get_ball().gety()
        
        posicaox[3] = posicaox[2] #guarda posicao antiga do setpoint
        posicaox[2] = posx #atualiza posicao atual do setpoint

        posicaoy[3] = posicaoy[2]
        posicaoy[2] = posy

        #print "Antigo" , posicaoy[1]
        #print "Novo", posicaoy[0] 

        print "Vetor velocidade da bolinha (", posicaox[0] - posicaox[1] , "       ", posicaoy[0] - posicaoy[1], ")"
        print "Vetor velocidade do setpoint (", posicaox[2] - posicaox[3] , "       ", posicaoy[2] - posicaoy[3], ")"

        '''
        adiciona_ponto(int(world.trave_left_upper[0]), int(world.trave_left_upper[1]),255,255,2555,'xg+20, yg')
        adiciona_ponto(int(world.trave_left_lower[0]), int(world.trave_left_lower[1]),255,255,2555,'xg+20, yg')
        return posx , posy


    def controle(self, world):
        xt, yt = self.defende(world)
        adiciona_ponto(int(xt), int(yt), 0,0,127, 'xt, yt')

        distancia_y = int(yt) - self.gety()
        distancia_x = int(xt) - self.getx()

        theta_biss = math.atan2(distancia_y, distancia_x)
        theta_biss *= 180.0 / 3.1415  # conversao p/ graus

        theta_pink = self.get_theta()

        theta_erro = theta_biss - theta_pink
        
        while theta_erro > 180.0:
            theta_erro -= 360.0
        while theta_erro < -180.0:
            theta_erro += 360.0

        # if theta_erro > 90 or theta_erro < -90:
        #     theta_pink += 180

        # theta_erro = theta_biss - theta_pink

        ro = math.sqrt(distancia_y * distancia_y + distancia_x * distancia_x)
        if ro == 0:
            ro = 1.0
        alfa = theta_erro * math.pi / 180.0  # conversao para radianos

        # ni eh a velocidade de avanco do modelo d Lyapunov

        if math.sqrt((self.gety()-world.get_ball().gety())**2 + (self.getx()-world.get_ball().getx())**2) < 10: #se a bola esta perto
            if world.get_ball().gety() > self.gety(): #se a bola esta mais baixo
                return -250, 250 #gira para um lado
            else:
                return 250, -250 #gira para o outro lado
        elif ro > 3:
            #return self.lyapunov(ro, alfa, 40.0, 50.0, 60.0) # original
            return self.lyapunov(ro, alfa, 250.0, 0.0, 12.0) #k_ni,k_alphaomega,fator_freio
        elif self.gety() > world.get_team_goal()[1]:
            theta_erro = 270 - theta_pink

            while theta_erro > 180.0:
                theta_erro -= 360.0
            while theta_erro < -180.0:
                theta_erro += 360.0
            alfa = theta_erro * math.pi / 180.0
            return self.lyapunov(ro, alfa, 0.0, 30.0, 1.0) #giro 70
        else:
            theta_erro = 90 - theta_pink

            while theta_erro > 180.0:
                theta_erro -= 360.0
            while theta_erro < -180.0:
                theta_erro += 360.0
            alfa = theta_erro * math.pi / 180.0
            # return self.lyapunov(ro, alfa, 0.0, 80.0, 1.0) # Funciona pro rob1
            return self.lyapunov(ro, alfa, 0.0, 30.0, 1.0) # funciona pro rob4 #giro 70