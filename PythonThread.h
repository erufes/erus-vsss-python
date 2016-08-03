#ifndef PYTHONTHREAD_H
#define PYTHONTHREAD_H

#include <QThread>
#include <QImage>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "opencv2/video/tracking.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/objdetect/objdetect.hpp"
#include "PythonAPI.h"

#include "World.h"
#include "Buffer.h"
#include "Utils.h"
#include "Configuracao.h"

class PythonThread : public QThread {
    Q_OBJECT

private:
    PythonAPI *pyAPI;
    Buffer<World> *bufferWorld;
    Buffer<cv::Mat> *bufferImagemProcessada;

    bool paused;

protected:
    void run();

public slots:
    void pauseGame(bool ativa);
    void inicioPenalty(int tipo);// 1 para ataque, 2 para defesa
    void updateBorders();
    void TeamColor(bool team);

public:
    PythonThread(Buffer<World> *bufferWorld, Buffer<cv::Mat> *bufferImagemProcessada);
    ~PythonThread();

signals:
    void newFrame(const QImage &frame);
};

#endif // PYTHONTHREAD_H
