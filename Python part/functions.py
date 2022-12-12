import Classes as Cl
import math


# def updateAll():
#    Cl

def anglVectors(a, b, c, d):
    dotProduct = a*c + b*d
    # for three dimensional simply add dotProduct = a*c + b*d  + e*f
    modOfVector1 = math.sqrt(a*a + b*b)*math.sqrt(c*c + d*d)
    # for three dimensional simply add modOfVector = math.sqrt( a*a + b*b + e*e)*math.sqrt(c*c + d*d +f*f)
    angle = dotProduct/modOfVector1
    #print("Cosθ =", angle)
    angleInDegree = math.degrees(math.acos(angle))
    #print("θ =", angleInDegree, "°")
    return angleInDegree
