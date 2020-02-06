#include "VideoProcessor.h"


VideoProcessor::VideoProcessor()
{
    VideoProcessor(0);
}

VideoProcessor::VideoProcessor(int n)
{
    cap = cv::VideoCapture(n);
}

VideoProcessor::~VideoProcessor()
{
    if(cap.isOpened())
        cap.release();
}

