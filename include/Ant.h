//#ifndef BaseAnt
//#define BaseAnt
#pragma once

#include "AntSimulator.h"
#include <stdlib.h>

#define PI 3.14159265

class BaseAnt
{
private:
    int AntSize = 10;
    int Antposition[2] = {0, 0};
    int AntDirection = 0;
    int FreedomVariable = 2;
    int AntSpeed = 2;
    //    AntSimulator &the_connected_sim;

public:
    int getSize() { return AntSize; };
    int getPos(int i) { return Antposition[i]; };
    int getDirection() { return AntDirection; };

    BaseAnt(){};

    void MoveForward()
    {
        //New x Position
        Antposition[0] = Antposition[0] + (cos(AntDirection * PI / 180) * AntSpeed);
        //New Y position
        Antposition[1] = Antposition[1] + (sin(AntDirection * PI / 180) * AntSpeed);
    };

    void moveRandom()
    {
        //Move the Ant in a direction with FreedomVariable as the Free will
        AntDirection = AntDirection + (rand() % (FreedomVariable * 2) - FreedomVariable);
        MoveForward();
    }
};

//#endif //BaseAnt