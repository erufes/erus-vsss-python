#ifndef BLOBPROCESSOR_H
#define BLOBPROCESSOR_H

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

#include <list>
#include <vector>

#include "Configuracao.h"

using namespace cv;
using namespace std;

typedef vector<Point> Contour;

class BlobProcessor
{
    Scalar colorLowerBound, colorUpperBound;
    Mat imageHsv;
    list<Scalar> results;
    Mat histogram;

    double orderedInsertion(list<Contour> &ls, Contour cnt, double area, unsigned int maxSize);

public:
    BlobProcessor(Mat &img, Scalar &colorLowerBound, Scalar &colorUpperBound);
    ~BlobProcessor();

    void setImage(Mat &img);
    void setColorLowerBound(Scalar &color);
    void setColorUpperBound(Scalar &color);

    void process(unsigned int n);
    void processBall(unsigned int n);

    list<Scalar> getResults();
    Mat getHistogram();
};

#endif // BLOBPROCESSOR_H
