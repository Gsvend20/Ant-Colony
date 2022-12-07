import numpy as np
import matplotlib as plt
from PIL import ImageShow as img
import Classes as Cl
import time
import cv2
Cl.mapsize = [700, 700]


def UpdateAll():
    Cl.UpdateAll()


def showall():
    Cl.showall()


ant_array_test = []
#Cl.hivelist = []
Cl.hivelist.append(Cl.Hive("Main", 0, 360, 5, 5, 10,
                           5000, Cl.mapsize[0]/2, Cl.mapsize[1]/2))
Cl.hivelist[0].spawnAnt(2)
ant_array_test.append(Cl.Ant('Henning', 0, 5, 0, 0))
# print(ant_array_test[0].name)
# print(ant_array_test[0].antPos(0))


blank_image = np.zeros((400, 400, 3), dtype="uint8")
#img = cv2.imread(blank_image, cv2.IMREAD_GRAYSCALE)
cv2.imshow("shitface", blank_image)
cv2.waitKey(500)

while True:
    t = time.time()
    # print(mainhive.antlist[0].Pos[0])
    # Cl.hivelist[0].showall()
    UpdateAll()
    showall()
    Cl.hivelist[0].food += 0.7
    # time.sleep(3)
    # print('looping')
    # print(Cl.hivelist[0].food)
    while time.time() < t+0.02:
        # print(time.time())
        Waiting = True


# time.sleep(1)  # sleep for 1 seconds
