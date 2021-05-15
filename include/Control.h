#include <Sensors.h>
#include "AntSimulator.h"
#include "Plants.h"

class BaseControl //ParentClass
{
private:
    Plant &OurPlant;

public:
    BaseControl(Plant &plant) : OurPlant(plant){};
};
