import math
import World

class Agent:
    def __init__(self):
        self.x = self.y = 0

    def update_position(self, (x, y)):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getxy(self):
        return int(self.getx()), int(self.gety())

    def distance_to(self, x, y):
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)

    def predicao_adaptativa(self, x):
        return 4
        #return 4.5 + (x - World.World.FIELD_LEFT) * (3.5 - 4.5) / (World.World.FIELD_RIGHT - World.World.FIELD_LEFT)