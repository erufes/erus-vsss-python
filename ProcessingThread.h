#ifndef PROCESSINGTHREAD_H
#define PROCESSINGTHREAD_H

#include <iostream>
#include <ctype.h>

#include <QThread>
#include <QImage>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "opencv2/video/tracking.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/objdetect/objdetect.hpp"

#include "Buffer.h"
#include "Configuracao.h"
#include "BlobProcessor.h"
#include "World.h"

class ProcessingThread : public QThread {
    Q_OBJECT

private:
    Buffer<cv::Mat> *buffer;
    Buffer<World> *bufferWorld;
    Buffer<cv::Mat> *bufferImagemProcessada;
    bool paused;
    QMutex m_mutex;

protected:
    void run();

public:
    ProcessingThread(Buffer<cv::Mat> *buffer, Buffer<World> *bufferWorld, Buffer<cv::Mat> *bufferImagemProcessada);
    double norma2(Scalar a, Scalar b);

public slots:
    void pause(bool b);
    void escolheCor(bool cor);//true = azul, false = amarelo
};

#endif // PROCESSINGTHREAD_H
