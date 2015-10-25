#include "CaptureThread.h"

CaptureThread::CaptureThread(Buffer<cv::Mat> *buffer, bool dropFramesIfFull) {
    this->buffer = buffer;
    this->dropFramesIfFull = dropFramesIfFull;
}

bool CaptureThread::connectToCamera() {
    bool ret = cap.open(0);

//    cap.set(CV_CAP_PROP_FRAME_WIDTH, 640);
//    cap.set(CV_CAP_PROP_FRAME_HEIGHT, 480);
//    cap.set(CV_CAP_PROP_FPS, 60);

    return ret;
}

bool CaptureThread::disconnectCamera() {
    if (isCameraConnected()) {
        cap.release();
        return true;
    } else {
        return false;
    }
}

bool CaptureThread::isCameraConnected() {
    return cap.isOpened();
}

void CaptureThread::run() {

    while (1) {

        // There are no frames to be used yet
        if (!cap.grab()) {
            continue;
        }

        cv::Mat frame;
        cap.retrieve(frame);
        cv::flip(frame,frame, -1);

        buffer->add(frame, dropFramesIfFull);
    }
}
