from .Agent import Agent
import math
from .World import *


class Player(Agent):

    def __init__(self, rid=None):
        self.xa_old = [0.0,0.0,0.0,0.0,0.0]
        self.ya_old = [0.0,0.0,0.0,0.0,0.0]
        self.xb_old = [0.0,0.0,0.0,0.0,0.0]
        self.yb_old = [0.0,0.0,0.0,0.0,0.0]
        self.xa = self.ya = self.xb = self.yb = 0
        self.theta_old = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        self.theta = 0
        self.medo_de_bater_na_parede = 30.0
        self.id = rid
        Agent.__init__(self)

############# Controlador

    #posicao anterior para KD
        self.xe_old = 0
        self.ye_old = 0
        self.te_old = 0

    #somatorio dos erros para o KI 
        self.erroX = 0
        self.erroY = 0
        self.erroT = 0

    def set_xe_old(self, xe):
        self.xe_old = xe

    def set_ye_old(self, ye):
        self.ye_old = ye

    def set_te_old(self, te):
        self.te_old = te

    def get_xe_old(self):
        return self.xe_old

    def get_ye_old(self):
        return self.ye_old

    def get_te_old(self):
        return self.te_old


    #funcoes do KI       

    def inc_sumErroX(self, erroX):
        self.erroX += erroX

    def inc_sumErroY(self, erroY):
        self.erroY += erroY

    def inc_sumErroT(self, erroT):
        self.erroT += erroT

    def get_sumErroX(self):
        return self.erroX

    def get_sumErroY(self):
        return self.erroY

    def get_sumErroT(self):
        return self.erroT

##########################

    def get_front(self):
        return self.xa, self.ya

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
        self.theta_old.insert(0,float(math.atan2(self.yb - self.ya, self.xb - self.xa)))
        self.theta_old.pop()
        self.theta = sum(self.theta_old)/15.0

    def update_xy(self):
        x = 0.5 * (self.xa + self.xb)
        y = 0.5 * (self.ya + self.yb)
        self.update_position((x, y))

    def set_position(self, ta, tb):
        self.xa_old.insert(0,float(ta[0]))
        self.xa_old.pop()
        self.ya_old.insert(0,float(ta[1]))
        self.ya_old.pop()
        self.xb_old.insert(0,float(tb[0]))
        self.xb_old.pop()
        self.yb_old.insert(0,float(tb[1]))
        self.yb_old.pop()

        mxa = sum(self.xa_old)/5.0
        mya = sum(self.ya_old)/5.0
        mxb = sum(self.xb_old)/5.0
        myb = sum(self.yb_old)/5.0

        self.set_front(mxa, mya)
        self.set_back(mxb, myb)

        self.update_theta()
        self.update_xy()

    def set_position_xyt(self, x, y, theta):
        self.set_xy(x,y)
        self.set_theta(theta)

    def get_theta(self):
        return self.theta

    def predicao_adaptativa(self, x, world):
        return (4.5 + (x - world.left_limit) * (3.5 - 4.5) / (world.right_limit - world.left_limit))*0.85

    def chuta(self, world):
        ball = world.get_ball()
        xb, yb = ball.predict_ball_method(self, world)
        xr, yr = self.getxy()
        xg, yg = world.get_right_goal()
        my_inf = 1e5
        ofensividade = self.campo_potencial(world)

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

        value = self.campo_potencial(world)


        grad_x = (world.campo_potencial_g(xb + 10.0, yb, self.medo_de_bater_na_parede) - value )
        grad_y = (world.campo_potencial_g(xb, yb + 10.0, self.medo_de_bater_na_parede) - value )


        norm_grad = math.sqrt(grad_x ** 2 + grad_y ** 2)
        if norm_grad != 0:
            grad_x /= norm_grad
            grad_y /= norm_grad

        curva_de_nivel_segura = 0.2  # Curva de nivel a partir da qual nao eh mais possivel manobrar o robo.


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
        
        v_r = (omega + ni)
        v_l = (-omega + ni)
   
        maior = max(abs(v_r),abs(v_l))

        if maior > 255.0:
            v_r = v_r * (255.0/maior)
            v_l = v_l * (255.0/maior)

        v_r = int(v_r)
        v_l = int(v_l)
        
        return v_r, v_l

    def controle(self, world):

        pd = world.get_def_player()
        xfront , yfront = pd.get_front()  #unidade das coordenadas eh cm
        xback , yback = pd.get_back()  #unidade das coordenadas eh cm
        pd_x , pd_y = pd.getx() , pd.gety()  #unidade das coordenadas eh cm
        xb, yb = world.get_ball().getxy() #unidade das coordenadas eh cm
    
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
        K = 255
        vr, vl = y[0][0]*K/vmax, y[1][0]*K/vmax  #mudei a constante para 255 antes era 100

        return int(vr), int(vl)

    def campo_potencial(self, mundo):
        #return (math.tanh((xr - right_upper[0])**2/medo_de_bater_na_parede**2)* math.tanh((xr - left_upper[0])**2/medo_de_bater_na_parede**2) * math.tanh((yr - right_lower[1])**2/medo_de_bater_na_parede**2) * math.tanh((yr - right_upper[1])**2/medo_de_bater_na_parede**2))/4.0
        xr, yr = self.getxy()
        dx = xr - mundo.left_goal[0]
        dy = yr - mundo.left_goal[1]

        ro = math.sqrt(dx**2+dy**2)
        ret = (math.tanh((xr - mundo.right_upper[0])**2/self.medo_de_bater_na_parede**2)* math.tanh((xr - mundo.left_upper[0])**2/self.medo_de_bater_na_parede**2) * math.tanh((yr - mundo.right_lower[1])**2/self.medo_de_bater_na_parede**2) * math.tanh((yr - mundo.right_upper[1])**2/self.medo_de_bater_na_parede**2))/(1-math.exp(-(ro**2)/8000.0))/4.0
        if ro < 100:
            ret = 0
        return ret

    def check_type(self):
        pass