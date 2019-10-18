from .Ball import *

class World:
    #TODO: update field constants

    #BIGULIN PRA ESQUERDA

    #LADO DE CAH
    # FIELD_LEFT = 194
    # FIELD_RIGHT = 600
    # FIELD_TOP = 83
    # FIELD_BOTTOM = 430

    #LADO DE LAH (medidas oficiais do campo)
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

        self.jogadores = {"Team" : {"GK" : list(), "DF" : list(), "FW" : list()}, "Enemies" : list()}
        self.ball = Ball()
    
    def remove_def_player(self, p):
        self.jogadores["Team"]["DF"].remove(p)
    
    def remove_atk_player(self, p):
        self.jogadores["Team"]["FW"].remove(p)
    
    def remove_gk_player(self, p):
        self.jogadores["Team"]["GK"].remove(p)

    def add_def_player(self, p):
        self.jogadores["Team"]["DF"].append(p)
    
    def add_atk_player(self, p):
        self.jogadores["Team"]["FW"].append(p)

    def add_gk_player(self, p):
        self.jogadores["Team"]["GK"].append(p)

    def get_def_player(self):
        return self.jogadores["Team"]["DF"] 

    def get_atk_player(self):
        return self.jogadores["Team"]["FW"] 

    def get_goalkeeper(self):
        return self.jogadores["Team"]["GK"] 

    def get_teammate(self, n):
        return self.jogadores["Team"][n]

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
    #Guilherme:  Versao para atualizacao de jogador usando, x,y,angle
    def update(self, p0_x, p0_y, p0_theta, p1_x, p1_y, p1_theta, p2_x, p2_y, p2_theta, pos_ball):

        #Goalkeeper // Atacante
        p0 = self.get_teammate(0)
        p0.set_position_xyt(p0_x, p0_y, p0_theta)

        #Player 1 // Zagueiro
        p1 = self.get_teammate(1)
        p1.set_position_xyt(p1_x, p1_y, p1_theta)

        #Player 2 // Goleiro
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
        print ("ola")
        print (self.FIELD_RIGHT)
        print (self.FIELD_LEFT)
        print (self.FIELD_TOP)
        print (self.FIELD_BOTTOM)
        print ("ola1")