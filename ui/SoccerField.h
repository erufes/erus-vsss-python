#ifndef SOCCERFIELD_H
#define SOCCERFIELD_H

#include <C:\opencv\build\include\opencv2\core\core.hpp>
#include <C:\opencv\build\include\opencv2\highgui\highgui.hpp>
#include <C:\opencv\build\include\opencv2\imgproc\imgproc.hpp>

using namespace cv;

class SoccerField
{
    Point2i upperLeftCorner, bottomRightCorner;

public:
    SoccerField();
    SoccerField(const Point2i &ulc, const Point2i &brc);
    ~SoccerField();

    Point2i getUpperLeftCorner() const;
    void setUpperLeftCorner(const Point2i &value);
    Point2i getBottomRightCorner() const;
    void setBottomRightCorner(const Point2i &value);
};

#endif // SOCCERFIELD_H
