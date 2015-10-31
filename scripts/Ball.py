import Agent
import math


class Ball(Agent.Agent):
    def __init__(self):
        #self.x_old, self.y_old = 0, 0
        self.x_old = [0.0,0.0,0.0,0.0,0.0]
        self.y_old = [0.0,0.0,0.0,0.0,0.0]
        self.x = self.y = 0

    def getxy_old(self):
        return self.x_old, self.y_old

    # def predict_ball_method(self, player):
    #     return self.x,self.y

    def predict_ball_method(self, player):
        mx = sum(self.x_old)/5.0
        my = sum(self.y_old)/5.0

        #vx_ball = self.getx() - self.x_old
        #vy_ball = self.gety() - self.y_old

        vx_ball = (self.getx() - mx)/2.0
        vy_ball = (self.gety() - my)/2.0

        norm_v_ball = math.sqrt(vx_ball**2 + vy_ball**2)

        if norm_v_ball < 2:
            cx_ball_predic = self.getx()
            cy_ball_predic = self.gety()
        else:
            vx_ball /= norm_v_ball
            vy_ball /= norm_v_ball

            dif_x = self.getx()-player.getx()
            dif_y = self.gety()-player.gety()
            ro_aux = math.sqrt(dif_x**2 + dif_y**2)

            c_magic = self.predicao_adaptativa(self.x)
            #k_pred = c_magic*ro_aux/80.0
            k_pred = c_magic*ro_aux/100.0

            cx_ball_predic = self.getx() + vx_ball * k_pred * norm_v_ball
            cy_ball_predic = self.gety() + vy_ball * k_pred * norm_v_ball
        return cx_ball_predic, cy_ball_predic

    def predict_ball_method_ofensive(self, player):
        mx = sum(self.x_old)/5.0
        my = sum(self.y_old)/5.0

        #vx_ball = self.getx() - self.x_old
        #vy_ball = self.gety() - self.y_old

        vx_ball = (self.getx() - mx)/2.0
        vy_ball = (self.gety() - my)/2.0

        norm_v_ball = math.sqrt(vx_ball**2 + vy_ball**2)

        """
        if norm_v_ball < 2:
            cx_ball_predic = self.getx()
            cy_ball_predic = self.gety()
        else:"""
        if(norm_v_ball == 0):
            norm_v_ball = 1
        vx_ball /= norm_v_ball
        vy_ball /= norm_v_ball

        dif_x = self.getx()-player.getx()
        dif_y = self.gety()-player.gety()
        ro_aux = math.sqrt(dif_x**2 + dif_y**2)

        c_magic = self.predicao_adaptativa(self.x)
        #k_pred = c_magic*ro_aux/80.0
        k_pred = c_magic*ro_aux/85.0

        cx_ball_predic = self.getx() + vx_ball * k_pred * norm_v_ball
        cy_ball_predic = self.gety() + vy_ball * k_pred * norm_v_ball
        
        return cx_ball_predic, cy_ball_predic

    """
    def predict_ball_method_ofensive(self, player):
        vx_ball = self.getx() - self.x_old
        vy_ball = self.gety() - self.y_old
        norm_v_ball = math.sqrt(vx_ball**2 + vy_ball**2)

        if norm_v_ball < 2:
            cx_ball_predic = self.getx()
            cy_ball_predic = self.gety()
        else:
            vx_ball /= norm_v_ball
            vy_ball /= norm_v_ball

            dif_x = self.getx()-player.getx()
            dif_y = self.gety()-player.gety()
            ro_aux = math.sqrt(dif_x**2 + dif_y**2)

            k_pred = 3.0 #1.0

            cx_ball_predic = self.getx() + vx_ball * k_pred * norm_v_ball
            cy_ball_predic = self.gety() + vy_ball * k_pred * norm_v_ball
        return cx_ball_predic, cy_ball_predic
    """

    def set_position(self, xy):
        #self.x_old, self.y_old = self.getxy()
        xo, yo = self.getxy()
        self.x_old.insert(0,float(xo))
        self.x_old.pop()
        self.y_old.insert(0,float(yo))
        self.y_old.pop()
        self.update_position(xy)