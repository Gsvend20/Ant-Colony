//#ifndef BaseHive
//#define BaseHive
#pragma once

#include <string>
#include <time.h>
#include "Ant.h"

BaseAnt ant;

class BaseHive
{
private:
    int HiveSize = 5;
    int Connected_Ants = 0;
    int HivePosition[2] = {0, 0};

public:
    int getSize() { return HiveSize; };
    int getPos(int i) { return HivePosition[i]; };
    void setPos(int x, int y)
    {
        HivePosition[0] = x;
        HivePosition[1] = y;
    };
    //double measure() override { return the_connected_sim.getLampValue(); };

    BaseHive(){};

    void CreateAnt(){};

    void UpdateAnts()
    {
        ant.moveRandom();
    };
};

//#endif //BaseHive