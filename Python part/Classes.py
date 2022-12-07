import random as rm
import numpy as np
import matplotlib.pyplot as plt
import cv2
mapsize = [700, 700]

img = np.zeros((mapsize[0], mapsize[1], 3), np.uint8)


foodlist = []
antlist = []
Phermonelist = []
#delpher =[]
hivelist = []


def UpdateAll():
    if len(foodlist) > 0:
        for i in range(len(foodlist)-1, 0, -1):
            answ = foodlist[i].update()
            if answ == False:
                delpher = foodlist.pop(i)
                del delpher
    if len(antlist) > 0:
        for i in range(len(antlist)-1, -1, -1):
            answ = antlist[i].update()
            if answ == False:
                delpher = antlist.pop(i)
                del delpher
    if len(Phermonelist) > 0:
        for i in range(len(Phermonelist)-1, -1, -1):
            answ = Phermonelist[i].update()
            if answ == False:
                delpher = Phermonelist.pop(i)
                del delpher
    if len(hivelist) > 0:
        for i in range(len(hivelist)-1, -1, -1):
            answ = hivelist[i].update()
            if answ == False:
                delpher = hivelist.pop(i)
                del delpher


def showall():
    img = np.zeros((mapsize[0], mapsize[0], 3), np.uint8)
    for i in range(0, len(Phermonelist)):  # Phermone
        cv2.rectangle(img, (int(Phermonelist[i].Pos[0]-Phermonelist[i].size[0]/2), int(Phermonelist[i].Pos[1]-Phermonelist[i].size[1]/2)), (
            int(Phermonelist[i].Pos[0]+Phermonelist[i].size[0]/2), int(Phermonelist[i].Pos[1]+Phermonelist[i].size[1]/2)), (int(Phermonelist[i].color[0]), int(Phermonelist[i].color[1]), int(Phermonelist[i].color[2])), 0)
    for i in range(0, len(foodlist)):  # FOOD
        cv2.rectangle(img, (int(foodlist[i].Pos[0]-foodlist[i].size[0]/2), int(foodlist[i].Pos[1]-foodlist[i].size[1]/2)), (
            int(foodlist[i].Pos[0]+foodlist[i].size[0]/2), int(foodlist[i].Pos[1]+foodlist[i].size[1]/2)), (foodlist[i].color[0], foodlist[i].color[1], foodlist[i].color[2]), 0)
    for i in range(0, len(antlist)):  # ANT
        cv2.warpAffine((cv2.rectangle(img, (int(antlist[i].Pos[0]-antlist[i].size[0]/2), int(antlist[i].Pos[1]-antlist[i].size[1]/2)), (
            int(antlist[i].Pos[0]+antlist[i].size[0]/2), int(antlist[i].Pos[1]+antlist[i].size[1]/2)), (antlist[i].color[0], antlist[i].color[1], antlist[i].color[2]), 0)), cv2.getRotationMatrix2D((50/2, 50/2), -antlist[i].angle, 1), (5, 5))  # , rotateCode=antlist[i].angle)
    for i in range(0, len(hivelist)):  # HIVE
        cv2.circle(img, (int(hivelist[i].HivePos[0]), int(
            hivelist[i].HivePos[1])), 5, (255, 0, 0), -1)

    cv2.imshow('image', img)
    cv2.waitKey(1)
    #print("antangle: "+str(antlist[0].angle))


class Ant:
    def __init__(self, name, age, visangle, Posx, Posy):
        self.name = name
        self.age = age
        self.visangle = visangle
        self.Pos = [Posx, Posy]
        #print('Pos is: ' + str(self.Pos))
        self.angle = rm.randrange(0, 360, 1)
        self.Phcolor = [rm.randrange(0, 255, 1), rm.randrange(
            0, 255, 1), rm.randrange(0, 255, 1)]
    speed = 1
    visrange = 10
    size = [1, 2]
    moveangle = 10
    mode = 'find'
    steps = 0
    color = [0, 255, 0]
    health = rm.randrange(50, 250, 1)

    def moveForward(self):
        self.angle += rm.randrange(0, (self.moveangle*2)+1, 1)-self.moveangle
        if (self.Pos[0]+self.speed*(np.cos(np.deg2rad(self.angle)))) > 0 and (self.Pos[0]+self.speed*(np.cos(np.deg2rad(self.angle)))) < mapsize[0] and (self.Pos[1]+self.speed*(np.sin(np.deg2rad(self.angle)))) > 0 and (self.Pos[1]+self.speed*(np.sin(np.deg2rad(self.angle)))) < mapsize[1]:
            self.Pos = [self.Pos[0]+self.speed*(np.cos(np.deg2rad(self.angle))),
                        self.Pos[1]+self.speed*(np.sin(np.deg2rad(self.angle)))]
            self.steps += 1
        # return self.Pos

    def antPos(self, x):
        print('Pos lenght is: '+str(len(self.Pos)))
        if x == 'x' or x == 0:
            print('x pos is: '+str(self.Pos[0]))
            # return self.Pos[0]
        else:
            print('y pos is: '+str(self.Pos[1]))
            # return self.Pos[1]

    def update(self):
        self.moveForward()
        self.health -= 1
        if self.steps > 5:
            Phermonelist.append(
                Phermone(self.Phcolor, self.Pos[0], self.Pos[1]))
            self.steps = 0
        if self.health <= 0:
            hivelist[0].food += 5
            return False
        else:
            return True

    def seePhermone(self):
        seelistP = []
        for i in range(0, len(antlist)):
            for j in range(0, len(Phermonelist)):
                pPos = [Phermonelist[j].Pos[0],
                        Phermonelist[j].Pos[1]]
                pdist = (np.sqrt(pPos ^ 2+pPos ^ 22))
                if pdist <= self.visrange:
                    seelistP.append(Phermonelist[j])
        seelistP.sort(
            reverse=True, key=Phermonelist[j].strength)

        if self.mode == 'find':
            for x in range(0, len(seelistP)):
                if seelistP[x].smell == self.mode:
                    self.moveForward()


class Hive:
    def __init__(self, name, age, visangle, spawnmax, spawntime, food, health, Posx, Posy):
        self.name = name
        self.age = age
        self.visangle = visangle
        self.spawnmax = spawnmax
        self.spawntime = spawntime
        self.food = food
        self.health = health
        self.HivePos = [Posx, Posy]
    ants = 0
    angle = 0
    speed = 0
    size = [2, 4]

    def spawnAnt(self, number):
        print('spawning ' + str(number) + ' ants!')

        for i in range(number):
            antlist.append(
                Ant("Anton", 0, 10, self.HivePos[0], self.HivePos[1]))
        # for i in range(self.ants, self.ants+number):
        #    ant = Ant('Anton', 0, 5, self.HivePos)
        #    self.ant.append(ant)
        self.ants += number
        print('total number of ants: '+str(self.ants))
        #print('total number of ants in list: '+str(len(antlist)))
        # print(antlist)

    def update(self):

        for i in range(0, len(antlist)):
            if antlist[i].Pos[0] <= self.HivePos[0]+5 and antlist[i].Pos[0] >= self.HivePos[0]+5 and antlist[i].Pos[1] <= self.HivePos[1]+5 and antlist[i].Pos[1] >= self.HivePos[1]-5:
                self.food += 10
        if self.food >= 5:
            spawnnumber = np.floor(self.food/5)
            #print('spawnnumber= '+str(spawnnumber))
            self.spawnAnt(int(spawnnumber))
            self.food -= spawnnumber*5
        self.health -= 1
        if self.health <= 0:
            return False
        else:
            return True


class Phermone:
    def __init__(self, color, Posx, Posy):
        self.color = color
        self.Pos = [Posx, Posy]
    lifetime = 50
    size = [2, 2]
    # color =

    def update(self):
        self.lifetime -= 1
        if self.lifetime <= 0:
            return False
        else:
            return True
