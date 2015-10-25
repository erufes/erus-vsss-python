#ifndef MEANSHIFTPROCESSOR_H
#define MEANSHIFTPROCESSOR_H

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "opencv2/video/tracking.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/objdetect/objdetect.hpp"

using namespace cv;

class MeanShiftProcessor
{
    Rect trackWindow;

public:
    MeanShiftProcessor();
    ~MeanShiftProcessor();
    static int hbins, sbins, w_camera, h_camera, robot_size;
    static int histSize[2];
    static float hranges[2];
    static float sranges[];
    static const float* ranges[2];
    static int channels[2];
    static TermCriteria criteria;

    void search(Mat frame);
};

#endif // MEANSHIFTPROCESSOR_H
