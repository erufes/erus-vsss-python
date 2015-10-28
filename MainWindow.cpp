#include "MainWindow.h"
#include "ui_MainWindow.h"
#include <iostream>
#include <QFileDialog>
#include <QMouseEvent>



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
    QString path = QFileDialog::getSaveFileName(0, "Save file", QDir::currentPath());
    Configuracao &conf = Configuracao::getInstance();
    conf.saveToFile(path.toUtf8().constData());
    //Configuracao &conf = Configuracao::getInstance();
    //conf.createColorElementXml();
//    conf.loadFile("config.xml");
//    std::cout << "haha";
}

void MainWindow::on_actionCarregar_triggered() {
    QString path = QFileDialog::getOpenFileName(0, "Load file", QDir::currentPath());
    Configuracao &conf = Configuracao::getInstance();
    conf.loadFile(path.toUtf8().constData());
    updateBorders();
}

void MainWindow::on_actionPenault_triggered()
{
    penalty();
}

void MainWindow::on_actionTime_Azul_triggered()
{
     escolheCor(true);
}

void MainWindow::on_actionTIme_Amarelo_triggered()
{
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
