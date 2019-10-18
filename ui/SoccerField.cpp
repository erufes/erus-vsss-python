#include "SoccerField.h"


SoccerField::SoccerField()
{
    upperLeftCorner = Point2i();
    bottomRightCorner = Point2i();
}

SoccerField::SoccerField(const Point2i &ulc, const Point2i &brc) {
    setUpperLeftCorner(ulc);
    setBottomRightCorner(brc);
}

SoccerField::~SoccerField()
{

}

Point2i SoccerField::getUpperLeftCorner() const
{
    return upperLeftCorner;
}

void SoccerField::setUpperLeftCorner(const Point2i &value)
{
    upperLeftCorner = value;
}

Point2i SoccerField::getBottomRightCorner() const
{
    return bottomRightCorner;
}

void SoccerField::setBottomRightCorner(const Point2i &value)
{
    bottomRightCorner = value;
}
