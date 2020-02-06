#include "ColorManagementThread.h"

#include "ProcessingThread.h"

ColorManagementThread::ColorManagementThread(Buffer<cv::Mat> *buffer)
    : m_stop(false) {
    this->buffer = buffer;
}

//ColorManagementThread::~ColorManagementThread() {
//}

void ColorManagementThread::run() {

    while(1) {
        cv::Mat mat = buffer->get();
        emit(newFrame(mat));

        QMutexLocker locker(&m_mutex);
        if(m_stop) {
            break;
        }
    }
}

void ColorManagementThread::stop() {
    QMutexLocker locker(&m_mutex);
    m_stop = true;
}




// Possivel solucao pra vida
//class Thread : public QThread
//{
//Q_OBJECT

//public:
//    Thread();
//signals:
//    void testSignal(QString message);
//slots:
//    void mTimeOut();
//protected:
//    void run();
//};

//Thread::Thread()
//{
//}

//void Thread::run()
//{
//    QTimer::singleShot(0, this, SLOT(mTimeOut()));

//    exec();
//}

//void Thread::mTimeOut()
//{
//    //do what You need in one step
//    emit(testSignal("hello world!"));
//    //do sleep and after start next step
//    QTimer::singleShot(1, this, SLOT(mTimeOut()));
//}
