#ifndef CONSTANTS_H
#define CONSTANTS_H

#include <opencv2/core/core.hpp>

using namespace cv;

Scalar getLowerLimitColorPlayer1() {
    return Scalar(56., 74.,244.);
}

Scalar getUpperLimitColorPlayer1() {
    return Scalar(71.,110.,255.);
}


#endif // CONSTANTS_H

