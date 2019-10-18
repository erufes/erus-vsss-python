#ifndef VIDEOPROCESSOR_H
#define VIDEOPROCESSOR_H

#include <C:\opencv\build\include\opencv2\core\core.hpp>
#include <C:\opencv\build\include\opencv2\highgui\highgui.hpp>
#include <C:\opencv\build\include\opencv2\imgproc\imgproc.hpp>
#include <iostream>

class VideoProcessor
{
    cv::VideoCapture cap;
    cv::Mat rawFrame, roiFrame;

public:
    VideoProcessor();
    VideoProcessor(int n);

    void loadNewFrame();
    cv::Mat getFrame();
    void setRoi();
    cv::Mat getRoiFrame();


    ~VideoProcessor();
};

#endif // VIDEOPROCESSOR_H
