#ifndef UTILS_H
#define UTILS_H

#include <cmath>

#include <QDebug>
#include <QImage>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "opencv2/video/tracking.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/objdetect/objdetect.hpp"

#include "Configuracao.h"

class Utils
{
public:
    float static pxToCm(int px);
    float static cmToPx(float cm);
    float static norm(cv::Point a, cv::Point b);
    static QImage cvMatToQImage(const cv::Mat &inMat);
};

#endif // UTILS_H
