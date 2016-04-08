#ifndef CALIBRACAOARENA_H
#define CALIBRACAOARENA_H

#include <QDialog>
#include <QLabel>
#include <QMessageBox>

#include "CalibracaoArenaThread.h"

namespace Ui {
class CalibracaoArena;
}

class CalibracaoArena : public QDialog
{
    Q_OBJECT

public:
    void mousePressEvent(QMouseEvent *ev);
    explicit CalibracaoArena(Buffer<cv::Mat> *buffer, QWidget *parent = 0);
    ~CalibracaoArena();

signals:
    void pauseProcessingThread(bool pausa);
    void stopThread();
    void updateBorders();

public slots:
    void updateFrame(const cv::Mat &frame);
    void reject();

private slots:
    void on_CalibracaoArena_finished(int result);

    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_4_clicked();

    void on_aplicar_clicked();

    void on_pushButton_5_clicked();

    void on_Quadrado_clicked();

    void on_Click_clicked();

    void on_lineEdit_10_cursorPositionChanged(int arg1, int arg2);

private:
    Ui::CalibracaoArena *ui;
    CalibracaoArenaThread *calibracaoArenaThread;
    QLabel label;
    QSemaphore *sem;
    cv::Mat frame;
    int posEditada;

    void setLabels(int n);
    void preencheCampos();
    void atualizaConfiguracao();
    cv::Vec3b pegaCorLower(int n);
    cv::Vec3b pegaCorUpper(int n);
    void alteraLimitesCor(int n, cv::Vec3b lower, cv::Vec3b upper, cv::Vec3b color);
    void setaCorLower(int n, cv::Vec3b color);
    void setaCorUpper(int n, cv::Vec3b color);
    void setPositionLeftUpper(int x, int y);
    void setPositionRightUpper(int x, int y);
    void setPositionRightLower(int x, int y);
    void setPositionLeftLower(int x, int y);
    void setFromConfig();
    cv::Scalar getPositionLeftUpper();
    cv::Scalar getPositionRightUpper();
    cv::Scalar getPositionRightLower();
    cv::Scalar getPositionLeftLower();
};



#endif // CALIBRACAO_ARENA

