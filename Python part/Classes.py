import random as rm
import numpy as np


class Ant:
    def __init__(self, name, age, visangle):
        self.name = name
        self.age = age
        self.visangle = visangle
    Pos = {2, 3}
    angle = 0
    speed = 1

    def moveForward(self):
        randangl = rm.randrange(-(self.visangle), self.visangle, 1)
        self.Pos = {self.Pos[0]+self.speed*(np.cos(self.angle+randangl)),
                    self.Pos[1]+self.speed*(np.sin(self.angle+randangl))}
        return self.Pos
