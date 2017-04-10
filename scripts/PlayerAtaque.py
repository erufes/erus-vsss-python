import Player
import math
import World
import numpy as np
import cv2
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
        # SAIR DA PAREDE 
        if self.getx() > world.FIELD_RIGHT and xb < self.getx():
            return self.getx() - 30, self.gety()

        if yb > world.FIELD_BOTTOM - distancia_pra_sair_da_parede or yb < world.FIELD_TOP + distancia_pra_sair_da_parede or xb > world.FIELD_RIGHT -distancia_pra_sair_da_parede or xb < world.FIELD_LEFT + distancia_pra_sair_da_parede:
            #print "aqui"         
            if self.gety() > world.FIELD_BOTTOM - distancia_pra_sair_da_parede and (theta_robo > 30 and theta_robo < 150) :
                return self.getx(),self.gety() -15
            elif self.gety() < world.FIELD_TOP + distancia_pra_sair_da_parede and (theta_robo > -150 and theta_robo < 30):
                return self.getx(),self.gety() +15
            if self.getx() > world.FIELD_RIGHT -distancia_pra_sair_da_parede -1 and (yb > yg-20 and yb < yg+20):
                a = world.FIELD_RIGHT - 15
                b = self.gety()
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
         #acaba sair da parede
        #a = a -5

        p = world.get_def_player()
        x,y = p.getx(),p.gety()

        adiciona_ponto(int(xg), int(yg+20),255,255,2555,'xg+20, yg')
        adiciona_ponto(int(xg), int(yg-20),255,255,2555,'xg-20, yg')
        distance_to_amiguinho = math.sqrt((x-self.getx())**2 + (y-self.gety())**2)

        if distance_to_amiguinho < 20:
            x,y = self.getx()+5,self.gety() 
            return int(x),int(y)
        return xb,yb
        #return a,b
#        Quando o jogador se aproxima muito da bola, o setpoint deve ficar atras da bola, garantindo que ele chute a bola
        sensibility = 1.5
        distance_to_ball = math.sqrt((xb-self.getx())**2 + (yb-self.gety())**2)
        if distance_to_ball < 25 and xb > self.getx():
            if(not(yb+ (yb - self.gety()) > yg + 20 or (yb+ (yb - self.gety()) < yg-20))): # so alterar o setpoint caso ajude a fazer gol.
                return (xb + sensibility*(xb-self.getx())), (yb+ sensibility*(yb - self.gety()))
            if(self.getx() - xg and self.gety() - yb): # faz gol na diagonal (sqn)
                if(yb > self.gety() and self.gety() < yg-20):#parte de cima do campo
                    if(math.atan2(self.gety() - (yg-20),(self.getx()-xg)) - math.atan2(self.gety() -(yg+20),(self.getx()-xg)) > math.atan2((self.getx() - xb),(self.gety() - yb))):
                        return (xb + sensibility*(xb-self.getx())), (yb+ sensibility*(yb - self.gety()))
                if(yb < self.gety() and self.gety() > yg+20 ):#parte de baixo do campo
                    if(math.atan2(self.gety() - (yg+20),(self.getx()-xg)) - math.atan2(self.gety() -(yg-20),(self.getx()-xg)) > math.atan2((self.getx() - xb),(self.gety() - yb))):
                        return (xb + sensibility*(xb-self.getx())), (yb+ sensibility*(yb - self.gety()))
            #if(yb < yg -20 and yb < self.gety()):
                #return a , b-15
            #if(yb > yg +20 and yb > self.gety()):
                #return a, b+15
        #return a, b

        '''cm = (self.getx() + 5) 
        raio = ((self.getx() - xb)**2 + (self.gety() - yb)**2)/2
        x_x0 = cm - (self.getx() + xb)/2
        y0 = (self.gety() + yb)/2
        c = x_x0**2 + y0**2-raio
        if(yb < self.gety()):
            y_final = y0 + (abs(y0**2 - c))**0.5
        else:
            y_final = y0 - (abs(y0**2 - c))**0.5
        #return a, b
        '''
        cm = math.pi/6
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
                return x_final , y_final    
        return a , b

    def kalman(self,world):
        meas=[]
        pred=[]
        mp = np.array((2,1), np.float32) # measurement
        tp = np.zeros((2,1), np.float32) # tracked / prediction
        kalman = cv2.KalmanFilter(4,2)
        kalman.measurementMatrix = np.array([[1,0,0,0],[0,1,0,0]],np.float32)
        kalman.transitionMatrix = np.array([[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]],np.float32)
        kalman.processNoiseCov = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],np.float32) * 0.03
        kalman = cv2.KalmanFilter(4,2)
        aux1 = 0.133333
        aux2 = 0.033333
        theta_ball_vel = math.atan2(aux1*aux2*vr,aux1*aux2*ve)
        xb, yb = self.chuta(world)
        theta_ball = math.atan2(yb,xb)
        mp = np.array([[np.float32(theta_ball_vel)],[np.float32(theta_ball)]])
        meas.append((theta_ball_vel,theta_ball))
        kalman.correct(mp)
        tp = kalman.predict()
        pred.append((int(tp[0]),int(tp[1])))
        return tp[0]





    def controle(self, world):

        pd = world.get_atk_player()
        xfront , yfront = pd.get_front()  #unidade das coordenadas eh cm
        xback , yback = pd.get_back()  #unidade das coordenadas eh cm
        pd_x , pd_y = pd.getx() , pd.gety()  #unidade das coordenadas eh cm
        xb, yb = world.get_ball().getxy() #unidade das coordenadas eh cm
        xb, yb = self.chuta(world)
        arq = open("posAtk.csv","a")
        arq.write(str(pd_x) + ", " + str(pd_y))
        arq.write("\n")
        arq.close()
        
        arq = open("ball.csv","a")
        arq.write(str(xb) + ", " + str(yb))
        arq.write("\n")
        arq.close()
        adiciona_ponto(int(pd_x),int(pd_y), 128, 200, 126, 'atacante',int(xb), int(yb)) # verde escuro




        #xb, yb = world.get_ball().predict_ball_method(self) #unidade das coordenadas eh cm
        #adiciona_ponto(int(xb), int(yb), 35, 100, 215, '')


        theta_jog = self.get_theta()
        theta_ball = math.atan2(yb,xb) # unidade rad
        #theta_ball = self.kalman(world)
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

        #constantes do controlador

        ####### KP ########
        KPx = 1
        KPy = 1
        KPt = 1
        
        ####### KD ########
        KDx = 0
        KDy = 0
        KDt = 0

        ####### KI ########
        KIx = 0
        KIy = 0
        KIt = 0

        #dado o sistema y = pseudoA*Matriz_erro obtem-se y que eh a velocidade da roda direita e velocidade da roda esquerda
        A = np.array([[math.cos(theta_jog)/2, math.cos(theta_jog)/2], [math.sin(theta_jog)/2, math.sin(theta_jog)/2],[1/D, -1/D]])
        pseudoA = np.linalg.pinv(A)
        Matriz_erro = (T)*np.array([[(xb - pd_x)/100], [(yb - pd_y)/100], [theta_erro]])

        errox_atual = Matriz_erro[0][0]
        erroy_atual = Matriz_erro[1][0]
        errot_atual = Matriz_erro[2][0]

        self.inc_sumErroX(errox_atual)
        self.inc_sumErroY(erroy_atual)
        self.inc_sumErroT(errot_atual)

        controladorPID = np.array([[KPx + KDx*(errox_atual - self.get_xe_old()) + KIx*self.get_sumErroX()], [KPy + KDy*(erroy_atual - self.get_ye_old()) + KIy*self.get_sumErroY()], [KPt + KDt*(errot_atual - self.get_te_old()) + KIt*self.get_sumErroT()]])

        self.set_xe_old(errox_atual)
        self.set_xe_old(erroy_atual)
        self.set_xe_old(errot_atual)

        '''print("Matriz de Erro\n")
        print(Matriz_erro)
        print("Controlador\n")
        print(controladorPID)
        Matriz_erro = Matriz_erro*controladorPID
        print("Final\n")
        print(Matriz_erro)'''
        

        y = pseudoA.dot(Matriz_erro)
        vmax = max(abs(y[0][0]), abs(y[1][0])) # pega a maior velocidade

        #como a velocidade foi parametrizada pela maior, K eh a maior velocidade que a roda pode assumir
        K = 100
        vr, vl = y[0][0]*K/vmax, y[1][0]*K/vmax  

        return int(vr), int(vl)