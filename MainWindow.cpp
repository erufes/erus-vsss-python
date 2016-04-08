#include "MainWindow.h"
#include "ui_MainWindow.h"
#include <iostream>
#include <QFileDialog>
#include <QMouseEvent>
#include "Utils.h"



MainWindow::MainWindow(PythonThread *pythonThread, ProcessingThread *processingThread, Buffer<cv::Mat> *bufferImagem, QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    numberOfFrames = 0;
    elapsedTimer = new QElapsedTimer();
    elapsedTimer->start();

    colorManagementWindow = NULL;
    this->pythonThread = pythonThread;
    QObject::connect(this, SIGNAL(updateBorders()), pythonThread, SLOT(updateBorders()));
    this->processingThread = processingThread;

    this->bufferImagem = bufferImagem;

    fpsLabel = new QLabel(this);
//    fpsLabel->setText("Vá se ferrar");
    ui->statusBar->addWidget(fpsLabel);

    std::cout << QDir::currentPath().toStdString() << std::endl;

    Configuracao &conf = Configuracao::getInstance();
    conf.loadFile("config.xml");
    updateBorders();


}
void MainWindow::mousePressEvent(QMouseEvent *ev) {

    if(ev->type() == QEvent::MouseButtonPress && Calibrando_Bordas)
    {
        QPoint p = ui->label->mapFrom(this, ev->pos());
        //std::cout << "x: " << p.x() << " " << "y: " << p.y() << std::endl;

        //std::cout << p.QPoint() << std::endl;
    }
    if(ev->type() == QEvent::MouseButtonPress && Medindo_Distancia)
    {
        QPoint t = ui->label->mapFrom(this, ev->pos());
        if(First_Click_Distance)
        {
            First_Click_Distance = false;
            Points_Distance[0] = t;
        }
        else
        {
            Points_Distance[1] = t;
            First_Click_Distance = true;
            float distance_px = MainWindow::Distance_Q_Point(Points_Distance[0],Points_Distance[1]);
            float distance_cm = Utils::pxToCm(distance_px);
            std::cout << distance_cm << std::endl;

        }
        //std::cout << "x: " << p.x() << " " << "y: " << p.y() << std::endl;

        //std::cout << p.QPoint() << std::endl;
    }

}

float MainWindow::Distance_Q_Point(const QPoint &a,const QPoint &b)
{
    float x = a.x() - b.x();
    float y = a.y() - b.y();
    return sqrt(x * x + y * y);
}

void MainWindow::updateFrame(const QImage &frame) {
    ui->label->setPixmap(QPixmap::fromImage(frame));

    ++numberOfFrames;
    if(elapsedTimer->elapsed() > 1000) {
        double fps = (float)numberOfFrames*1000/elapsedTimer->elapsed();
        fpsLabel->setText(QString::number(fps));
        elapsedTimer->restart();
        numberOfFrames = 0;
    }
}

MainWindow::~MainWindow() {
    delete elapsedTimer;
    delete ui;
}

void MainWindow::on_actionCores_triggered() {
    colorManagementWindow = new ColorManagement(bufferImagem, this);
    QObject::connect(colorManagementWindow, SIGNAL(pauseProcessingThread(bool)), processingThread, SLOT(pause(bool)));
    colorManagementWindow->pauseProcessingThread(true);
    colorManagementWindow->show();
}

void MainWindow::on_actionNovo_triggered() {
}

void MainWindow::on_actionParar_triggered()
{
    pauseGame(true);
}

void MainWindow::on_actionIniciar_triggered()
{
    pauseGame(false);
}

void MainWindow::on_actionSalvar_triggered()
{
    Configuracao &conf = Configuracao::getInstance();
    conf.saveToFile(name_file_load.c_str());
}

void MainWindow::on_actionCarregar_triggered() {
    QString path = QFileDialog::getOpenFileName(0, "Load file", QDir::currentPath());
    Configuracao &conf = Configuracao::getInstance();
    conf.loadFile(path.toUtf8().constData());
    name_file_load = path.toUtf8().toStdString();
    std::cout << name_file_load << std::endl;
    updateBorders();
}

void MainWindow::on_actionPenault_triggered()
{
    penalty(1);
}

void MainWindow::on_actionTime_Azul_triggered()
{
    ui->actionTIme_Amarelo->setText("Time Amarelo");
    ui->actionTime_Azul->setText("Time Azul (Selecionado)");
    ui->lineEdit->setText("Time Azul");
    escolheCor(true);
}

void MainWindow::on_actionTIme_Amarelo_triggered()
{
    ui->actionTIme_Amarelo->setText("Time Amarelo(Selecionado)");
    ui->actionTime_Azul->setText("Time Azul");
    ui->lineEdit->setText("Time Amarelo");
    escolheCor(false);
}

void MainWindow::on_actionBordas_da_arena_triggered()
{
    calibracaoArenaWindow = new CalibracaoArena(bufferImagem, this);
    QObject::connect(calibracaoArenaWindow, SIGNAL(pauseProcessingThread(bool)), processingThread, SLOT(pause(bool)));
    QObject::connect(calibracaoArenaWindow, SIGNAL(updateBorders()), pythonThread, SLOT(updateBorders()));
    calibracaoArenaWindow->pauseProcessingThread(true);
    calibracaoArenaWindow->show();

}

void MainWindow::on_actionPenalty_defesa_triggered()
{
    penalty(2);
}

void MainWindow::on_actionSalvar_como_triggered()
{
    QString path = QFileDialog::getSaveFileName(0, "Save file", QDir::currentPath());
    Configuracao &conf = Configuracao::getInstance();
    conf.saveToFile(path.toUtf8().constData());
    //Configuracao &conf = Configuracao::getInstance();
    //conf.createColorElementXml();
//    conf.loadFile("config.xml");
//    std::cout << "haha";
}

void MainWindow::on_actionFechar_triggered()
{
    std::cout << "foda-se" << std::endl;
    this->close();
}

void MainWindow::on_actionDistancias_triggered()
{
    Medindo_Distancia = true;
    First_Click_Distance = true;
}


void MainWindow::on_actionFlip_triggered()
{
    Configuracao &conf = Configuracao::getInstance();
    if(conf.getStateFlip())
    {
        conf.setStateFlip(false);
        ui->actionFlip->setText("Flip (OFF)");
        ui->label_atacando->setText("<-- Atacando");
    }
    else
    {

        conf.setStateFlip(true);
        ui->actionFlip->setText("Flip (ON)");
        ui->label_atacando->setText("Atacando -->");
    }
}
