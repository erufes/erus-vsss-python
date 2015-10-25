#include "BlobProcessor.h"
#include <iostream>
#include <Utils.h>

#define M_PI    3.141592653589793238462643383279502884L

// image should be already in HSV color format
BlobProcessor::BlobProcessor(Mat &img, Scalar &colorLowerBound, Scalar &colorUpperBound)
{
    imageHsv = img;
    this->colorLowerBound = colorLowerBound;
    this->colorUpperBound = colorUpperBound;
    results = list<Scalar>();
}

BlobProcessor::~BlobProcessor()
{

}

void BlobProcessor::setImage(Mat &img) {
    imageHsv = img;
}

void BlobProcessor::setColorLowerBound(Scalar &color) {
    this->colorLowerBound = color;
}

void BlobProcessor::processBall(unsigned int n) {
    Configuracao& conf = Configuracao::getInstance();

    if(n == 0)
        return;

    cv::Mat maskRange1, maskRange2;

    cv::Scalar lowerRange1(0, colorLowerBound[1], colorLowerBound[2]), upperRange1(colorLowerBound[0], colorUpperBound[1], colorUpperBound[2]);
    cv::inRange(imageHsv, lowerRange1, upperRange1, maskRange1);

    cv::Scalar lowerRange2(colorUpperBound[0], colorLowerBound[1], colorLowerBound[2]), upperRange2(255, colorUpperBound[1], colorUpperBound[2]);
    cv::inRange(imageHsv, lowerRange2, upperRange2, maskRange2);

    Mat imageMask;
    cv::addWeighted(maskRange1, 1, maskRange2, 1, 0, imageMask);

    calcHist(&imageHsv, 1, conf.channels, imageMask, histogram, 2, conf.histSize, conf.ranges);
    normalize(histogram, histogram, 0, 255, CV_MINMAX);

    vector<Contour> contours;
    vector<Vec4i> hierarchy;
    findContours(imageMask, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0));

    list<Contour> bestCountours = list<Contour>();
    double worstArea = -1;

    for(vector<Contour>::iterator it = contours.begin(); it != contours.end(); it++) {
       double cntArea = contourArea(*it);

       //if(worstArea <= cntArea) {
           worstArea = orderedInsertion(bestCountours, *it, cntArea, n);
       //}
    }

    for (list<Contour>::iterator it = bestCountours.begin(); it != bestCountours.end(); it++) {
        Moments m = moments(*it);
        Scalar pos(m.m10/m.m00, m.m01/m.m00);

        if(isnan(pos[0]) || isnan(pos[1])) {
            pos[0] = pos[1] = 0;
        }

        results.insert(results.begin(), pos);
    }
}

/*
void BlobProcessor::processBall(unsigned int n) {
    Configuracao& conf = Configuracao::getInstance();

    if(n == 0)
        return;

    cv::Mat maskRange1, maskRange2;

    cv::Scalar lowerRange1(0, colorLowerBound[1], colorLowerBound[2]), upperRange1(colorLowerBound[0], colorUpperBound[1], colorUpperBound[2]);
    cv::inRange(imageHsv, lowerRange1, upperRange1, maskRange1);

    cv::Scalar lowerRange2(colorUpperBound[0], colorLowerBound[1], colorLowerBound[2]), upperRange2(255, colorUpperBound[1], colorUpperBound[2]);
    cv::inRange(imageHsv, lowerRange2, upperRange2, maskRange2);

    Mat imageMask;
    cv::addWeighted(maskRange1, 1, maskRange2, 1, 0, imageMask);

//    calcHist(&imageHsv, 1, conf.channels, imageMask, histogram, 2, conf.histSize, conf.ranges);
//    normalize(histogram, histogram, 0, 255, CV_MINMAX);

    cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(3, 3));
    cv::morphologyEx(imageMask, imageMask, cv::MORPH_CLOSE, kernel);
    cv::morphologyEx(imageMask, imageMask, cv::MORPH_OPEN, kernel);

    cv::GaussianBlur(imageMask, imageMask, cv::Size(9, 9), 2, 2);

//    vector<Vec3f> circles;
//    cv::HoughCircles( imageMask, circles, CV_HOUGH_GRADIENT, 1, imageMask.rows/8, 20, 25);

//    std::cout << "num circulos: " << circles.size() << std::endl;

//    if(circles.empty()) {
//        results.insert(results.begin(), Scalar(0, 0));
//    } else {
//        results.insert(results.begin(), Scalar(circles.front()[0], circles.front()[1]));
//    }

    vector<Contour> contours;
    vector<Vec4i> hierarchy;
    findContours(imageMask, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0));

    list<Contour> bestCountours = list<Contour>();
    double worstArea = -1;
    unsigned long long circular = 0;
    unsigned long long ncircular = 0;

    RotatedRect bestEllipse;
    double bestK = 60000000;

    for(vector<Contour>::iterator it = contours.begin(); it != contours.end(); it++) {
//       Contour output;
//       approxPolyDP(*it, output, 0.01*arcLength(*it, true), true);

//       if(output.size() <= 15) {
//           ncircular++;
////           std::cout << "Nao circular..." << std::endl;
//           continue;
//       } else {
//           circular++;
//           std::cout << output.size() << std::endl;
//       }

        Contour c = *it;
        double cntArea = contourArea(*it);
        if(c.size() < 5
//                || Utils::pxToCm(cntArea) < M_PI
                //                || Utils::pxToCm(cntArea) > M_PI *2.3*2.3
//                                || cntArea < 50
                ){
            continue;
        }

        RotatedRect elipse = fitEllipse(*it);
        const double w = elipse.size.width;
        const double h = elipse.size.height;

        double areaEllipse = M_PI * w * h / 4.0;

        double k = abs(cntArea/areaEllipse - 1);
//        if(k > 1) {
//            k = 2-k;
//        }

//        k = 1-k;

        if(areaEllipse == 0) {
            continue;
        }

        double f = 0.0;
        if( w > h) {
            f = w/h;
        } else {
            f = h/w;
        }

        if(f < 1.5 && k < bestK) {
//            std::cout << "Area ellipse: " << areaEllipse << std::endl;
//            std::cout << "Area contorno: " << cntArea << std::endl;
//            std::cout << "k: " << k << std::endl;
            bestEllipse = elipse;
            bestK = k;
        }

       //if(worstArea <= cntArea) {
//           worstArea = orderedInsertion(bestCountours, *it, cntArea, n);
       //}
    }

//    std::cout << "FIM" << std::endl;

    results.insert(results.begin(), Scalar(bestEllipse.center.x, bestEllipse.center.y));

//    std::cout << "circular: " << circular << std::endl;
//    std::cout << "nao circular: " << ncircular << std::endl;

//    exit(0);

//    for (list<Contour>::iterator it = bestCountours.begin(); it != bestCountours.end(); it++) {
//        Moments m = moments(*it);
//        Scalar pos(m.m10/m.m00, m.m01/m.m00);

//        if(isnan(pos[0]) || isnan(pos[1])) {
//            pos[0] = pos[1] = 0;
//        }

//        results.insert(results.begin(), pos);
//    }
}
*/
void BlobProcessor::setColorUpperBound(Scalar &color) {
    this->colorUpperBound = color;
}

void BlobProcessor::process(unsigned int n) {
    Configuracao& conf = Configuracao::getInstance();

    if(n == 0)
        return;

    Mat imageMask;

    inRange(imageHsv, colorLowerBound, colorUpperBound, imageMask);

    calcHist(&imageHsv, 1, conf.channels, imageMask, histogram, 2, conf.histSize, conf.ranges);
    normalize(histogram, histogram, 0, 255, CV_MINMAX);

    vector<Contour> contours;
    vector<Vec4i> hierarchy;
    findContours(imageMask, contours, hierarchy, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE, Point(0, 0));

    list<Contour> bestCountours = list<Contour>();
    double worstArea = -1;

    for(vector<Contour>::iterator it = contours.begin(); it != contours.end(); it++) {
       double cntArea = contourArea(*it);

       //if(worstArea <= cntArea) {
           worstArea = orderedInsertion(bestCountours, *it, cntArea, n);
       //}
    }

    for (list<Contour>::iterator it = bestCountours.begin(); it != bestCountours.end(); it++) {
        Moments m = moments(*it);
        Scalar pos(m.m10/m.m00, m.m01/m.m00);

        if(isnan(pos[0]) || isnan(pos[1])) {
            pos[0] = pos[1] = 0;
        }

        results.insert(results.begin(), pos);
    }

    //cout << n << " " << contours.size() << " " << bestCountours.size() << endl;
}

double BlobProcessor::orderedInsertion(list<Contour> &ls, Contour cnt, double area, unsigned int maxSize) {


//    if(maxSize > 1)
//        cout << "max: " << maxSize << endl;

    if(ls.empty()) {
//        if(maxSize > 1)
//            cout << "aki" << endl;
      ls.push_back(cnt);
      return area;
    }

    for(list<Contour>::iterator it = ls.begin(); it != ls.end(); it++) {
        double itArea = contourArea(*it);
        if(area > itArea) {
//            if(maxSize > 1)
//                cout << "aki" << endl;
            ls.insert(it, cnt);
            if(ls.size() > maxSize) {
                ls.pop_back();
            }
            return contourArea(ls.back());
        }
    }

    if(maxSize > 1) {
        ls.push_back(cnt);

        if(ls.size() > maxSize)
            ls.pop_back();
    }

    return contourArea(ls.back());
}

list<Scalar> BlobProcessor::getResults() {
    return results;
}

