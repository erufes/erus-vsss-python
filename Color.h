#ifndef COLOR_H
#define COLOR_H

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace cv;

class Color
{
    Vec3b lowerBound, upperBound;

public:
    Color();
    Color(Vec3b &lb, Vec3b &ub);
    ~Color();

    void setLowerBound(Vec3b &lb);
    Vec3b getLowerBound() const;

    void setUpperBound(Vec3b &ub);
    Vec3b getUpperBound() const;
};

#endif // COLOR_H
