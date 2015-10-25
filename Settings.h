#ifndef SETTINGS_H
#define SETTINGS_H

#include "Color.h"
#include "SoccerField.h"

#include <cstring>
#include <iostream>

#define     COLOR_BLUE          0
#define     COLOR_YELLOW        1
#define     COLOR_ORANGE        2
#define     COLOR_1             3
#define     COLOR_2             4
#define     COLOR_3             5

using namespace std;

class Settings
{
    Color *colors[6];
    Color blue, yellow, orange, color1, color2, color3;
    SoccerField soccerField;

public:
    Settings();
    Settings(const char *fileName);
    ~Settings();

    Color getBlue() const;
    void setBlue(const Color &value);

    Color getYellow() const;
    void setYellow(const Color &value);

    Color getOrange() const;
    void setOrange(const Color &value);

    Color getColor1() const;
    void setColor1(const Color &value);

    Color getColor2() const;
    void setColor2(const Color &value);

    Color getColor3() const;
    void setColor3(const Color &value);

    SoccerField getSoccerField() const;
    void setSoccerField(const SoccerField &value);
};

#endif // SETTINGS_H
