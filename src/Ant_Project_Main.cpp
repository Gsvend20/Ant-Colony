//#include "imgui.h"      // necessary for ImGui::*, imgui-SFML.h doesn't include imgui.h
//#include "imgui-SFML.h" // for ImGui::SFML::* functions and SFML-specific overloads

#include "AntSimulator.h"
#include "Ant.h"
#include "Hive.h"
#include <Control.h>
#include <iostream>
#include <string>
#include <thread>
#include <chrono>
#include <time.h>
#include <SFML/Graphics.hpp>

//time_t timer;
std::string;

int WorldLength = 900;
int WorldHeight = 900;

int main(int argc, char const *argv[])
{
    std::cout << "Hello!"
              << "\nl";

    BaseHive hive;

    // create the window
    sf::RenderWindow window(sf::VideoMode(WorldLength, WorldHeight), "Ant Colony Simulator");
    window.setFramerateLimit(2);

    hive.setPos(WorldLength / 2, WorldHeight / 2);
    std::cout << "Hive Position is : " << hive.getPos(0) << "," << hive.getPos(1) << "\nl";

    //Hive
    sf::RectangleShape HiveVisual{sf::Vector2f{(float)ant.getSize(), (float)ant.getSize()}};
    HiveVisual.setFillColor(sf::Color::Green);
    HiveVisual.setOrigin(ant.getSize() / 2, ant.getSize() / 2);
    HiveVisual.setPosition(hive.getPos(0), hive.getPos(1));

    //Ant
    sf::RectangleShape TestAnt{sf::Vector2f{(float)ant.getSize() / 2, (float)ant.getSize()}};
    TestAnt.setFillColor(sf::Color::Red);
    TestAnt.setOrigin(ant.getSize() / 2, ant.getSize() / 2);
    TestAnt.setPosition(hive.getPos(0), hive.getPos(1));

    sf::Clock deltaClock;

    while (window.isOpen())
    {
        //Call Control
        //Call Simulation
        clock_t startTime = clock();

        hive.UpdateAnts();
        TestAnt.setPosition(hive.getPos(0), hive.getPos(1));
        /*
    Get values from sensors
    See if changes is needed
    Edit if nessesary
    */

        // check all the window's events that were triggered since the last
        // iteration of the loop
        sf::Event event;
        while (window.pollEvent(event))
        {
            // "close requested" event: we close the window
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // clear the window with black color
        window.clear();

        // draw everything here...
        //window.draw(my_tomato_view);
        window.draw(HiveVisual);
        window.draw(TestAnt);

        // end the current frame
        window.display();
        std::cout << "Ant Position is : " << ant.getPos(0) << "," << ant.getPos(1) << "\nl";

        //Calculate the running speed
        clock_t endTime = clock();
        clock_t clockTicksTaken = endTime - startTime;
        double timeInSeconds = clockTicksTaken / (double)CLOCKS_PER_SEC;
    }

    return 0;
}

/*
lock_t startTime = clock();
doSomeOperation();
clock_t endTime = clock();
clock_t clockTicksTaken = endTime - startTime;
double timeInSeconds = clockTicksTaken / (double) CLOCKS_PER_SEC;

*/