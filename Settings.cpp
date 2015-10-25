#include "Settings.h"


Settings::Settings(const char *fileName) {

}

Settings::Settings() {

}

Settings::~Settings()
{

}

Color Settings::getBlue() const
{
    return blue;
}

void Settings::setBlue(const Color &value)
{
    blue = value;
}

Color Settings::getYellow() const
{
    return yellow;
}

void Settings::setYellow(const Color &value)
{
    yellow = value;
}

Color Settings::getOrange() const
{
    return orange;
}

void Settings::setOrange(const Color &value)
{
    orange = value;
}

Color Settings::getColor1() const
{
    return color1;
}

void Settings::setColor1(const Color &value)
{
    color1 = value;
}

Color Settings::getColor2() const
{
    return color2;
}

void Settings::setColor2(const Color &value)
{
    color2 = value;
}

Color Settings::getColor3() const
{
    return color3;
}

void Settings::setColor3(const Color &value)
{
    color3 = value;
}

SoccerField Settings::getSoccerField() const
{
    return soccerField;
}

void Settings::setSoccerField(const SoccerField &value)
{
    soccerField = value;
}

