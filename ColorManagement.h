#ifndef COLORMANAGEMENT_H
#define COLORMANAGEMENT_H

#include <QDialog>
#include <QLabel>
#include <QMessageBox>

#include "ColorManagementThread.h"

namespace Ui {
class ColorManagement;
}

class ColorManagement : public QDialog
{
    Q_OBJECT

public:
    void mousePressEvent(QMouseEvent *ev);
    explicit ColorManagement(Buffer<cv::Mat> *buffer, QWidget *parent = 0);
    ~ColorManagement();

signals:
    void pauseProcessingThread(bool pausa);
    void stopThread();

public slots:
    void updateFrame(const cv::Mat &frame);
    void reject();

private slots:
    void on_ColorManagement_finished(int result);
    void on_pushButtonAzul_clicked();
    void on_pushButtonAmarelo_clicked();
    void on_pushButtonLaranja_clicked();
    void on_pushButtonCor1_clicked();
    void on_pushButtonCor2_clicked();
    void on_pushButtonCor3_clicked();

    void on_mostrarFiltroCheckBox_stateChanged(int arg1);

    void on_salvar_clicked();

    void on_reset_clicked();

    void on_label_linkActivated(const QString &link);

private:
    Ui::ColorManagement *ui;
    ColorManagementThread *colorManagementThread;
    QLabel label;
    QSemaphore *sem;
    cv::Mat frame;
    int corEditada;
    bool first_click = true;
    int old_pos[2];
    bool showFilter;

    void setLabels(int n);
    void preencheCampos();
    void atualizaConfiguracao();
    cv::Vec3b pegaCorLower(int n);
    cv::Vec3b pegaCorUpper(int n);
    void alteraLimitesCor(int n, cv::Vec3b lower, cv::Vec3b upper, cv::Vec3b color);
    void setaCorLower(int n, cv::Vec3b color);
    void setaCorUpper(int n, cv::Vec3b color);
};

#endif // COLORMANAGEMENT_H
