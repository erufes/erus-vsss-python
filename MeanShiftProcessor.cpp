#include "MeanShiftProcessor.h"

MeanShiftProcessor::MeanShiftProcessor()
{
    this-> = 30;
  /*  hbins = 30, sbins = 32, w_camera = 480 , h_camera = 640, robot_size = 60;
    trackWindow = Rect( 0, 0, h_camera, w_camera);*/
}

MeanShiftProcessor::~MeanShiftProcessor()
{

}

void MeanShiftProcessor::search(Mat frame) {

    Mat roi(frame, trackWindow);

    Mat hsv;
    cvtColor(frame, hsv, CV_BGR2HSV); // create the hsv
  /*  calcBackProject(&hsv, 1, channels, roi_hist, dst, ranges);
    meanShift(dst, track_window, criteria);
    rectangle(frame, track_window, CV_RGB(0, 255, 0), 2); // shows on screen a green rectangle to check where is the robot.
    cvtColor(roi, hsv_roi ,CV_BGR2HSV); // create the new hsv roi
    inRange(hsv_roi, Scalar(56., 74.,244.), Scalar(71.,110.,255.), mask); // search in the new hsv_roi the color and put at the mask 1.
    inRange(hsv_roi, Scalar(16., 126.,150.), Scalar(25.,180.,255.), mask2); // search in the new hsv_roi the color and put at the mask 2.
    calcHist(&hsv_roi, 1, channels, mask, roi_hist, 2, histSize, ranges);
*/}

