import random as rm
import numpy as np
#import matplotlib.pyplot as plt
import cv2
import functions as f
mapsize = [700, 700]


def takethird(elem):
    return elem[2]


img = np.zeros((mapsize[0], mapsize[1], 3), np.uint8)
preimg = img
counter = 1

foodcolor = [0, 255, 0]
homecolor = [255, 0, 0]
roamcolor = [0, 0, 255]
fightcolor = [10, 20, 30]

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
    global counter
    #preimg = img
    img = np.zeros((mapsize[0], mapsize[0], 3), np.uint8)
    for i in range(0, len(Phermonelist)):  # Phermone
        img[Phermonelist[i].Pos[0]][Phermonelist[i].Pos[1]] = (
            Phermonelist[i].color[0], Phermonelist[i].color[1], Phermonelist[i].color[2])
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
    imgname = 'Images/IMG'+str(counter)+'.png'
    cv2.imwrite(imgname, img,)
    counter += 1
    cv2.waitKey(1)
    #print("antangle: "+str(antlist[0].angle))


class Ant:
    def __init__(self, name, age, visangle, Posx, Posy):
        self.name = name
        self.age = age
        self.visangle = visangle
        self.Pos = [Posx, Posy]
        #print('Pos is: ' + str(self.Pos))
        self.angle = 180  # rm.randrange(0, 360, 1)
    speed = 1
    visrange = 50
    size = [1, 2]
    moveangle = 10
    mode = 'roam'
    Phcolor = roamcolor
    steps = 0
    color = [125, 240, 14]
    health = 100

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

    def scanArea(self):
        seelistP = []
        fullimg = preimg
        if self.mode == "food":
            #np.where(img >= foodcolor, 255, 0)
            pPhemFind = foodcolor
        elif self.mode == "home":
            pPhemFind = homecolor
        elif self.mode == "roam":
            pPhemFind = roamcolor
        elif self.mode == "fight":
            pPhemFind = fightcolor
        for i in range(int(self.Pos[0]-self.visrange), int(self.Pos[0]+self.visrange), 1):
            for j in range(int(self.Pos[1]-self.visrange), int(self.Pos[1]+self.visrange), 1):
                if abs(f.anglVectors(np.cos(self.angle), np.sin(self.angle), i-self.Pos[0], j-self.Pos[1])) < self.angle and (img[i, j, 0] == pPhemFind[0] or img[i, j, 1] > 0 or img[i, j, 2] > 0):
                    seelistP.append(
                        [i, j, (np.sqrt(np.power(i-self.Pos[0], 2)+np.power(j-self.Pos[1], 2)))])
        if len(seelistP) > 0:
            seelistP.sort(
                reverse=True, key=takethird)
            #self.angle += 1 *(self.angle -f.anglVectors(self.Pos[0], self.Pos[1], pPos[0], pPos[1]))
            self.angle = f.anglVectors(
                self.Pos[0], self.Pos[1], i, j)
        print('list of points'+str(seelistP))

    def update(self):
        self.scanArea()
        self.moveForward()
        #self.health -= 1
        if self.steps > 5:
            Phermonelist.append(
                Phermone(color=self.Phcolor, Posx=self.Pos[0], Posy=self.Pos[1], mode=self.mode))
            self.steps = 0
        # if self.health <= 0:
        #    hivelist[0].food += 5
        #    return False
        # else:
        #    return True

    def seePhermone(self):
        seelistP = []
        for j in range(0, len(Phermonelist)):
            pPos = [Phermonelist[j].Pos[0],
                    Phermonelist[j].Pos[1]]
            pdist = (np.sqrt(np.power(pPos[0], 2)+np.power(pPos[1], 2)))
            if pdist <= self.visrange and Phermonelist[j].mode == self.mode and f.anglVectors(self.Pos[0], self.Pos[1], pPos[0], pPos[1]) <= (self.angle + self.visangle) and f.anglVectors(self.Pos[0], self.Pos[1], pPos[0], pPos[1]) >= (self.angle - self.visangle):
                seelistP.append(Phermonelist[j])
        if len(seelistP) > 0:
            seelistP.sort(
                reverse=True, key=seelistP.strength)
            #self.angle += 1 *(self.angle -f.anglVectors(self.Pos[0], self.Pos[1], pPos[0], pPos[1]))
            self.angle = f.anglVectors(
                self.Pos[0], self.Pos[1], pPos[0], pPos[1])


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
    def __init__(self, color, Posx, Posy, mode):
        self.color = color
        self.mode = mode
        self.Pos = [Posx, Posy]
    strength = 50
    size = [2, 2]
    # color =

    def update(self):
        self.strength -= 1
        if self.strength <= 0:
            return False
        else:
            return True
