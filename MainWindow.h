#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QLabel>
#include <QElapsedTimer>

#include <opencv2\core\core.hpp>
#include <opencv2\highgui\highgui.hpp>

#include "Buffer.h"
#include "ColorManagement.h"
#include "PythonThread.h"
#include "ProcessingThread.h"
#include "CalibracaoArena.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT
    bool Calibrando_Bordas = false;
    bool Medindo_Distancia = false;
    bool Trocar_Atacante = false;
    bool First_Click_Distance = false;
    bool Team_Azul = false;
    QPoint Points_Distance[2];
    std::string name_file_load;

public:
    void mousePressEvent(QMouseEvent *ev);
    explicit MainWindow(PythonThread *pythonThread, ProcessingThread *processingThread, Buffer<cv::Mat> *bufferImagem, QWidget *parent = 0);
    ~MainWindow();

public slots:
    void updateFrame(const QImage &frame);
    void trajetoria(cv::Mat &frame,cv::Point ponto_final, cv::Point ponto_atual,cv::Scalar cor,bool lado);// true para esquerda


private slots:

    float Distance_Q_Point(const QPoint &, const QPoint &get);

    void on_actionCores_triggered();

    void on_actionNovo_triggered();

    void on_actionParar_triggered();

    void on_actionIniciar_triggered();

    void on_actionSalvar_triggered();

    void on_actionCarregar_triggered();

    void on_actionPenault_triggered();

    void on_actionTime_Azul_triggered();

    void on_actionTIme_Amarelo_triggered();

    void on_actionBordas_da_arena_triggered();

    void on_actionPenalty_defesa_triggered();

    void on_actionSalvar_como_triggered();

    void on_actionFechar_triggered();

    void on_actionDistancias_triggered();

    void on_actionFlip_triggered();

    void on_actionTrocar_Atacante_triggered();

    void on_actionSobre_triggered();

    void on_actionTroca_Goleiro_Defesa_triggered();

private:
    Ui::MainWindow *ui;
    QLabel label;
    QLabel *fpsLabel;

    Buffer<cv::Mat> *bufferImagem;

    int numberOfFrames;
    QElapsedTimer *elapsedTimer;    

    CalibracaoArena *calibracaoArenaWindow;
    ColorManagement *colorManagementWindow;

    PythonThread *pythonThread;
    ProcessingThread *processingThread;

signals:
    void pauseGame(bool ativa);
    void penalty(int tipo);// 1 para ataque e 2 para defesa
    void escolheCor(bool cor);
    void TeamColor(bool cor); // true para azul
    void updateBorders();
};

#endif // MAINWINDOW_H
