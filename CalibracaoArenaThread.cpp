#include "CalibracaoArenaThread.h"

#include "ProcessingThread.h"

CalibracaoArenaThread::CalibracaoArenaThread(Buffer<cv::Mat> *buffer)
    : m_stop(false) {
    this->buffer = buffer;
}

//ColorManagementThread::~ColorManagementThread() {
//}

void CalibracaoArenaThread::run() {

    while(1) {
        cv::Mat mat = buffer->get();
        emit(newFrame(mat));

        QMutexLocker locker(&m_mutex);
        if(m_stop) {
            break;
        }
    }
}

void CalibracaoArenaThread::stop() {
    QMutexLocker locker(&m_mutex);
    m_stop = true;
}
