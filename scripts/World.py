import PlayerAtaque
import PlayerDefesa
import Player
from Ball import *
import Goalkeeper
import cv2


class World:
    #TODO: update field constants

    #BIGULIN PRA ESQUERDA

    #LADO DE CAH
    # FIELD_LEFT = 194
    # FIELD_RIGHT = 600
    # FIELD_TOP = 83
    # FIELD_BOTTOM = 430

    #LADO DE LAH
    FIELD_LEFT = 85.0 * 0.36
    FIELD_RIGHT = 555.0 * 0.36
    FIELD_TOP = 50.0 * 0.36
    FIELD_BOTTOM = 450.0 * 0.36

    right_goal = (FIELD_RIGHT,(FIELD_TOP+FIELD_BOTTOM)*.5)
    left_goal = (FIELD_LEFT,(FIELD_TOP+FIELD_BOTTOM)*.5)
    right_upper = (FIELD_RIGHT,FIELD_TOP)
    left_upper = (FIELD_LEFT,FIELD_TOP)
    right_lower = (FIELD_RIGHT, FIELD_BOTTOM)
    left_lower = (FIELD_LEFT, FIELD_BOTTOM)

    trave_left_upper = (FIELD_LEFT, int((FIELD_BOTTOM - FIELD_TOP)/3.0) + FIELD_TOP)
    trave_left_lower = (FIELD_LEFT, int((FIELD_BOTTOM - FIELD_TOP)*2/3.0) + FIELD_TOP)
    trave_right_upper = (FIELD_RIGHT, int((FIELD_BOTTOM - FIELD_TOP)/3.0) + FIELD_TOP)
    trave_right_lower = (FIELD_RIGHT, int((FIELD_BOTTOM - FIELD_TOP)*2/3.0) + FIELD_TOP)

    def __init__(self):
        # Frendly goal: 0 to left and 1 to right
        self.goal = 0

        self.team = [PlayerAtaque.PlayerAtaque('3'), PlayerDefesa.PlayerDefesa('2') , Goalkeeper.Goalkeeper('1')]
        self.enemies = [Player.Player(), Player.Player(), Player.Player()]
        self.ball = Ball()

        # TODO: find information about game states
        self.game_state = None
    def get_def_player(self):
        return self.team[1] # TODO cuidado! Se mudar acima muda aki!!!

    def get_atk_player(self):
        return self.team[0] # TODO cuidado! Se mudar acima muda aki!!!

    def get_goalkeeper(self):
        return self.team[2] # TODO cuidado! Se mudar acima muda aki!!!

    def get_teammate(self, n):
        return self.team[n]

    def get_team_goal(self):
        if self.goal == 0:
            return self.left_goal
        else:
            return self.right_goal

    def get_enemy_goal(self):
        if self.goal != 0:
            return self.left_goal
        else:
            return self.right_goal

    def get_ball(self):
        return self.ball

    def get_right_goal(self):
        return self.right_goal

    def campo_potencial(self, player):
        #return (math.tanh((xr - right_upper[0])**2/medo_de_bater_na_parede**2)* math.tanh((xr - left_upper[0])**2/medo_de_bater_na_parede**2) * math.tanh((yr - right_lower[1])**2/medo_de_bater_na_parede**2) * math.tanh((yr - right_upper[1])**2/medo_de_bater_na_parede**2))/4.0
        xr, yr = player.getxy()
        dx = xr - self.left_goal[0]
        dy = yr - self.left_goal[1]

        ro = math.sqrt(dx**2+dy**2)
        ret = (math.tanh((xr - self.right_upper[0])**2/player.medo_de_bater_na_parede**2)* math.tanh((xr - self.left_upper[0])**2/player.medo_de_bater_na_parede**2) * math.tanh((yr - self.right_lower[1])**2/player.medo_de_bater_na_parede**2) * math.tanh((yr - self.right_upper[1])**2/player.medo_de_bater_na_parede**2))/(1-math.exp(-(ro**2)/8000.0))/4.0
        if ro < 100:
            ret = 0
        # print ret
        return ret

    def campo_potencial_g(self, xr, yr, medo_de_bater_na_parede):
        #return (math.tanh((xr - right_upper[0])**2/medo_de_bater_na_parede**2)* math.tanh((xr - left_upper[0])**2/medo_de_bater_na_parede**2) * math.tanh((yr - right_lower[1])**2/medo_de_bater_na_parede**2) * math.tanh((yr - right_upper[1])**2/medo_de_bater_na_parede**2))/4.0
        dx = xr - self.right_goal[0]
        dy = yr - self.right_goal[1]
        ro = math.sqrt(dx**2+dy**2)
        if ro < 100:
            return 0
        return (math.tanh((xr - self.right_upper[0])**2/medo_de_bater_na_parede**2)* math.tanh((xr - self.left_upper[0])**2/medo_de_bater_na_parede**2) * math.tanh((yr - self.right_lower[1])**2/medo_de_bater_na_parede**2) * math.tanh((yr - self.right_upper[1])**2/medo_de_bater_na_parede**2))/(1-math.exp(-(ro**2)/8000.0))/4.0

    @staticmethod
    def is_contour_outside_field(cnt):
        c = 35
        x,y,w,h = cv2.boundingRect(cnt)
        if x < World.FIELD_LEFT-c or y < World.FIELD_TOP-c or x+w > World.FIELD_RIGHT+c or y+h > World.FIELD_BOTTOM+c:
            return True
        else:
            return False

    """
    #Guilherme: Funcao criada para atualizar o world. substitui a funcao vm.process_frame(world)
    def update(self, p0_front, p0_back, p1_front, p1_back, p2_front, p2_back, pos_ball):

        #Goalkeeper
        p0 = self.get_teammate(0)
        p0.set_position(p0_front, p0_back)

        #Player 1
        p0 = self.get_teammate(1)
        p0.set_position(p1_front, p1_back)

        #Player 2
        p0 = self.get_teammate(2)
        p0.set_position(p2_front, p2_back) 

        # Update Ball
        ball = self.get_ball()
        ball.set_position(pos_ball)
    """
    #Guilherme:  Versao para atualizacao de jogador usando, x,y,angle
    def update(self, p0_x, p0_y, p0_theta, p1_x, p1_y, p1_theta, p2_x, p2_y, p2_theta, pos_ball):

        #Goalkeeper
        p0 = self.get_teammate(0)
        p0.set_position_xyt(p0_x, p0_y, p0_theta)

        #Player 1
        p1 = self.get_teammate(1)
        p1.set_position_xyt(p1_x, p1_y, p1_theta)

        #Player 2
        p2 = self.get_teammate(2)
        p2.set_position_xyt(p2_x, p2_y, p2_theta) 

        # Update Ball
        ball = self.get_ball()
        ball.set_position(pos_ball)

    def updateField(self, fieldRight, fieldLeft, fieldTop, fieldBottom):
        self.FIELD_RIGHT = fieldRight
        self.FIELD_LEFT = fieldLeft
        self.FIELD_TOP = fieldTop
        self.FIELD_BOTTOM = fieldBottom
        self.right_goal = (self.FIELD_RIGHT,(self.FIELD_TOP+self.FIELD_BOTTOM)*.5)
        self.left_goal = (self.FIELD_LEFT,(self.FIELD_TOP+self.FIELD_BOTTOM)*.5)
        self.right_upper = (self.FIELD_RIGHT,self.FIELD_TOP)
        self.left_upper = (self.FIELD_LEFT,self.FIELD_TOP)
        self.right_lower = (self.FIELD_RIGHT, self.FIELD_BOTTOM)
        self.left_lower = (self.FIELD_LEFT, self.FIELD_BOTTOM)

        self.trave_left_upper = (self.FIELD_LEFT, (self.FIELD_BOTTOM - self.FIELD_TOP)/3.0 + self.FIELD_TOP)
        self.trave_left_lower = (self.FIELD_LEFT, (self.FIELD_BOTTOM - self.FIELD_TOP)*2/3.0 + self.FIELD_TOP)
        self.trave_right_upper = (self.FIELD_RIGHT, (self.FIELD_BOTTOM - self.FIELD_TOP)/3.0 + self.FIELD_TOP)
        self.trave_right_lower = (self.FIELD_RIGHT, (self.FIELD_BOTTOM - self.FIELD_TOP)*2/3.0 + self.FIELD_TOP)
        print self.FIELD_RIGHT
        print self.FIELD_LEFT
        print self.FIELD_TOP
        print self.FIELD_BOTTOM

