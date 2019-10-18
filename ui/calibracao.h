#ifndef CALIBRACAO_H
#define CALIBRACAO_H

#include <iostream>
#include <ctype.h>
#include "opencv2/video/tracking.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/highgui/highgui.hpp"

using namespace cv;
using namespace std;

class calibracao{
    Scalar color1LowerBound(255, 255, 255);
    Scalar color1UpperBound(0, 0, 0);
    Scalar color2LowerBound(255, 255, 255);
    Scalar color2UpperBound(0, 0, 0);
    Scalar color3LowerBound(255, 255, 255);
    Scalar color3UpperBound(0, 0, 0);
    Scalar TeamLowerBound(255, 255, 255);
    Scalar TeamUpperBound(0, 0, 0);
    Scalar ballLowerBound(255, 255, 255);
    Scalar ballUpperBound(0, 0, 0);
    int mouse_click=0;
    Mat resImage;
    bool showMask = false;
    int k;
    public:
    Mat frame, hsv_roi, mask_team,mask_ball, mask2,mask3,mask4, roi_hist, hierarchy,hsv, dst;
    void CallBackFunc(int event, int x, int y, int flags, void* userdata);
    void setColorFunc();
}
#endif // CALIBRACAO_H

