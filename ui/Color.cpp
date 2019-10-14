#include "Color.h"

Color::Color()
{
    lowerBound = Vec3b(0, 0, 0);
    upperBound = Vec3b(255, 255, 255);
}

Color::Color(Vec3b &lb, Vec3b &ub) {
    lowerBound = lb;
    upperBound = ub;
}

Color::~Color()
{

}

void Color::setLowerBound(Vec3b &lb) {
    lowerBound = lb;
}

Vec3b Color::getLowerBound() const {
    return lowerBound;
}

void Color::setUpperBound(Vec3b &ub) {
    upperBound = ub;
}

Vec3b Color::getUpperBound() const {
    return upperBound;
}
