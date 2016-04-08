import Agent
import math
import World


class Player(Agent.Agent):

    def __init__(self, rid=None):
        self.xa = self.ya = self.xb = self.yb = 0
        self.theta = 0
        self.medo_de_bater_na_parede = 30.0;
        self.id = rid

    def get_id(self):
        return self.id

    # Front = Blue and back = colored
    def set_front(self, x, y):
        self.xa = x
        self.ya = y

    def get_front(self):
        return self.xa, self.ya

    def set_back(self, x, y):
        self.xb = x
        self.yb = y

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def set_theta(self, theta):
        self.theta = theta

    def get_back(self):
        return self.xb, self.yb

    def update_theta(self):
        self.theta = math.atan2(self.yb - self.ya, self.xb - self.xa)

    def update_xy(self):
        # distancia_y = int(yt) - 0.5*(int(cy_pink)+int(cy_team))
        #distancia_x = int(xt) - 0.5*(int(cx_pink)+int(cx_team))
        x = 0.5 * (self.xa + self.xb)
        y = 0.5 * (self.ya + self.yb)
        self.update_position((x, y))

    def set_position(self, (xa, ya), (xb, yb)):
        self.set_front(xa, ya)
        self.set_back(xb, yb)

        self.update_theta()
        self.update_xy()

    def set_position_xyt(self, x, y, theta):
        self.set_xy(x,y)
        self.set_theta(theta)

    def get_theta(self):
        return self.theta*180.0/3.1415

    def predicao_adaptativa(self, x, world):
        return (4.5 + (x - world.left_limit) * (3.5 - 4.5) / (world.right_limit - world.left_limit))*0.85

    def chuta(self, world):
        ball = world.get_ball()
        xb, yb = ball.predict_ball_method(self)
        xr, yr = self.getxy()
        xg, yg = world.get_right_goal()
        my_inf = 1e5
        ofensividade = world.campo_potencial(self)

        d_East = abs(xb - world.FIELD_RIGHT)
        d_West = abs(xb - world.FIELD_LEFT)
        d_South = abs(yb - world.FIELD_BOTTOM)
        d_North = abs(yb - world.FIELD_TOP)

        d_Best = d_East
        pto_inf = (my_inf, (world.FIELD_BOTTOM+world.FIELD_TOP)/2)

        if d_West < d_Best:
            pto_inf = (-my_inf, (world.FIELD_BOTTOM+world.FIELD_TOP)/2)
            d_Best = d_West

        if d_North < d_Best:
            pto_inf = ((world.FIELD_RIGHT + world.FIELD_LEFT)/2, -my_inf)
            d_Best = d_North

        if d_South < d_Best:
            pto_inf = ((world.FIELD_RIGHT + world.FIELD_LEFT)/2, my_inf)
            d_Best = d_South

        value = world.campo_potencial(self)


        grad_x = (world.campo_potencial_g(xb + 10.0, yb, self.medo_de_bater_na_parede) - value )
        grad_y = (world.campo_potencial_g(xb, yb + 10.0, self.medo_de_bater_na_parede) - value )


        norm_grad = math.sqrt(grad_x ** 2 + grad_y ** 2);
        if norm_grad != 0:
            grad_x /= norm_grad
            grad_y /= norm_grad

        curva_de_nivel_segura = 0.2  # Curva de nivel a partir da qual nao eh mais possivel manobrar o robo.


        # cv2.circle(frame,(     int(grad_x + xb_real)   ,   int(grad_y + yb_real)    ),5,(200,200,50),-1)
        posx = xb
        posy = yb

        ro = math.sqrt((xb - xr) ** 2 + (yb - yr) ** 2)
        norma_Vdif = math.sqrt((xg - xb) ** 2 + (yg - yb) ** 2)
        Vdifx = (xg - xb) / norma_Vdif

        Vdifx = (xg - xb) / norma_Vdif
        Vdify = (yg - yb) / norma_Vdif

        if (world.campo_potencial_g(xr, yr, self.medo_de_bater_na_parede) < 0.08):  # se estou muito perto da parede, vou pro centro.
            posx = (int((world.FIELD_RIGHT-world.FIELD_LEFT) / 2) + world.FIELD_LEFT)
            posy = (int((world.FIELD_BOTTOM-world.FIELD_TOP) / 2) + world.FIELD_TOP)


        elif (world.campo_potencial_g(xb, yb, self.medo_de_bater_na_parede) < 0.15):  # bola na parede, bato do lado
            posx = xb
            posy = yb

        else:
            avalia_func = world.campo_potencial_g(xr, yr, self.medo_de_bater_na_parede)

            ajuste_bloqueante_x = -grad_x * (0.80 * ro)
            ajuste_bloqueante_y = -grad_y * (0.80 * ro)

            ajuste_ofensivo_x = -Vdifx * (0.80 * ro)
            ajuste_ofensivo_y = -Vdify * (0.80 * ro)

            posx = xb + (1 - avalia_func) * ajuste_bloqueante_x + avalia_func * ajuste_ofensivo_x
            posy = yb + (1 - avalia_func) * ajuste_bloqueante_y + avalia_func * ajuste_ofensivo_y

        return int(posx), int(posy)

    #esta funcao recebe dois parametros: ro - distancia em pixels // alfa - erro angular em radianos
#esta funcao ja aciona os motores!
#mais info: igordeoliveiranunes@gmail.com

    def lyapunov(self, ro, alfa, Kni, K_alfa_omega, fator_freio):
        #Kni eh a maxima velocidade frontal do robo proporcional a [pwm]/[m/s]
        #K_alfa_omega: proporcional a [pwm]/[rad]
        #fator_freio: valor adimensional feito para compensar o decaimento demorado do tanh em funcao de ro


        ni = Kni * math.tanh(ro/fator_freio) * math.cos(alfa) #avanco em 
        #omega = K_alfa_omega*alfa + Kni * (math.tanh(ro/fator_freio)/(ro/fator_freio))*math.sin(alfa)*math.cos(alfa) #giro

        if ro == 0:
            omega = 0.0
        else:
            omega = K_alfa_omega*alfa + Kni * (math.tanh(ro/fator_freio)/(ro/fator_freio))*math.sin(alfa)*math.cos(alfa) #giro
        
#        v_r = int((R_robot * omega + ni)/1.3)
#        v_l = int((-R_robot * omega + ni)/1.3)

        v_r = (omega + ni)
        v_l = (-omega + ni)

        #print "antes, vr, vl = ", v_l, v_r
        
        maior = max(abs(v_r),abs(v_l))

        if maior > 255.0:
            v_r = v_r * (255.0/maior)
            v_l = v_l * (255.0/maior)

        """
        if abs(v_r) > 255.0:
            v_r = v_r * (255.0/abs(v_r))
            v_l = v_l * (255.0/abs(v_r))
        
        
        if abs(v_l) > 255.0:
            v_l = v_l * (255.0/abs(v_l))
            v_r = v_r * (255.0/abs(v_l))
        """
    
        v_r = int(v_r)
        v_l = int(v_l)
        
        """
        if v_r > 255:
            v_r = 255
        if v_r < -255:
            v_r = -255

        if v_l > 255:
            v_l = 255
        if v_l < -255:
            v_l = -255
        """
        
        #print "depois, vr, vl = ", v_l, v_r
        
        return v_r, v_l



    def new_lyapunov():
        return 0,0
    def controle(self, world):
        (xt, yt) = self.chuta(world)
        distancia_y = int(yt) - self.gety()
        distancia_x = int(xt) - self.getx()

        theta_ball = math.atan2(distancia_y, distancia_x )
        theta_ball *= 180.0/3.1415#conversao p/ graus

        theta_pink = self.get_theta()

        theta_erro = theta_ball - theta_pink

        while theta_erro > 180.0:
            theta_erro -= 360.0
        while theta_erro < -180.0:
            theta_erro += 360.0

        ro = math.sqrt(distancia_y*distancia_y + distancia_x*distancia_x)
        if ro == 0:
            ro = 1.0
        alfa = theta_erro *math.pi/180.0 #conversao para radianos

        # ni eh a velocidade de avanco do modelo d Lyapunov

        #return self.lyapunov(ro, alfa, 140.0, 200.0, 45.0)
        return self.lyapunov(ro, alfa, 100.0, 185.0, 45.0)



