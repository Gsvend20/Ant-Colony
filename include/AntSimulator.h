#include <string>
#include <time.h>
//#include <Sensors.h>

class AntSimulator //Class
{
private:
    double currentTime = 0;

public:
    bool getTimeValue() { return currentTime; };
    void SetTime(int hour, int min) { currentTime = currentTime + hour + (min / 60); };

    void SimulateTime(int HourGot){};
};
