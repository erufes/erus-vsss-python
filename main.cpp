#include "MainWindow.h"
#include "Settings.h"
#include "CaptureThread.h"
#include "World.h"
#include "PythonAPI.h"
#include "Pythonthread.h"
#include "ProcessingThread.h"

#include <iostream>

#include <QApplication>

using namespace std;
using namespace cv;

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

    // Buffer serve para transito de imagens de CaptureThread para ProcessingThread
    Buffer<Mat> buffer(1);
    Buffer<Mat> bufferImagemProcessada(1);

    // Serve para envio de dados da ProcessingThread para PythonThread
    Buffer<World> bufferWorld(1);

    CaptureThread captureThread(&buffer, true);
    captureThread.connectToCamera();
    ProcessingThread processingThread(&buffer, &bufferWorld, &bufferImagemProcessada);
    PythonThread pythonThread(&bufferWorld, &bufferImagemProcessada);

    MainWindow w(&pythonThread, &processingThread, &buffer);
    w.show();

    QObject::connect(&pythonThread, SIGNAL(newFrame(QImage)), &w, SLOT(updateFrame(QImage)));
    QObject::connect(&w, SIGNAL(pauseGame(bool)), &pythonThread, SLOT(pauseGame(bool)));
    QObject::connect(&w, SIGNAL(penalty(int)), &pythonThread, SLOT(inicioPenalty(int)));
    QObject::connect(&w, SIGNAL(escolheCor(bool)), &processingThread, SLOT(escolheCor(bool)));

    captureThread.start();
    processingThread.start();
    pythonThread.start();

    return a.exec();
}


//int main(int argc, char *argv[]) {

//    int parametros[] = {50, 50, 0, 70, 70, 0, 100, 100, 0, 120, 120, 0};
//    PythonAPI *pyAPI;
//    cout << "aki" << endl;
//    pyAPI = new PythonAPI("main");
//    cout << "aki2" << endl;
//    while (1) {
//        pyAPI->callFunctionRun(parametros);
//    }

//       return 0;
//}
