#include <string>
#include <time.h>

class BaseHive
{
private:
    int HiveSize = 5;
    int Connected_Ants = 0;
    int HivePosition[2] = {0, 0};

public:
    //double measure() override { return the_connected_sim.getLampValue(); };

    void CreateAnt(){};
};