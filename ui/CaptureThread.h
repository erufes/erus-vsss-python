#ifndef CAPTURETHREAD_H
#define CAPTURETHREAD_H

#include <QThread>
#include <opencv2\core\core.hpp>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\highgui.hpp>
#include <opencv2\videoio.hpp>
#include <opencv2\opencv.hpp>


#include "Buffer.h"

class CaptureThread : public QThread {
    Q_OBJECT

private:
    Buffer<cv::Mat> *buffer;
    bool dropFramesIfFull;
    cv::VideoCapture cap;

protected:
    void run();

public:
    CaptureThread(Buffer<cv::Mat> *buffer, bool dropFramesIfFull = false);
    bool connectToCamera();
    bool disconnectCamera();
    bool isCameraConnected();
};

#endif // CAPTURETHREAD_H
