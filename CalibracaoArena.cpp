#include "CalibracaoArena.h"
#include "ui_CalibracaoArena.h"
#include "Configuracao.h"
#include "Utils.h"

#include <QMouseEvent>
#include <iostream>

CalibracaoArena::CalibracaoArena(Buffer<cv::Mat> *buffer, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::CalibracaoArena), posEditada(-1)
{
    ui->setupUi(this);
    setModal(true);

    calibracaoArenaThread = new CalibracaoArenaThread(buffer);
    qRegisterMetaType< cv::Mat >("cv::Mat");
    QObject::connect(calibracaoArenaThread, SIGNAL(newFrame(cv::Mat)), this, SLOT(updateFrame(cv::Mat)));
    QObject::connect(this, SIGNAL(stopThread()), calibracaoArenaThread, SLOT(stop()));
    calibracaoArenaThread->start();

    setFromConfig();

    //preencheCampos();
}

void CalibracaoArena::updateFrame(const cv::Mat &frame) {
    this->frame = frame;

    cv::Mat imageToShow = frame;

    cv::Point ll(getPositionLeftLower()[0], getPositionLeftLower()[1]);
    cv::circle(imageToShow, ll, 5, cv::Scalar(255, 0, 0), 5);

    cv::Point rl(getPositionRightLower()[0], getPositionRightLower()[1]);
    cv::circle(imageToShow, rl, 5, cv::Scalar(255, 0, 0), 5);

    cv::Point lu(getPositionLeftUpper()[0], getPositionLeftUpper()[1]);
    cv::circle(imageToShow, lu, 5, cv::Scalar(255, 0, 0), 5);

    cv::Point ru(getPositionRightUpper()[0], getPositionRightUpper()[1]);
    cv::circle(imageToShow, ru, 5, cv::Scalar(255, 0, 0), 5);

    QImage drawableImage = Utils::cvMatToQImage(imageToShow);
    ui->label->setPixmap(QPixmap::fromImage(drawableImage));
}

void CalibracaoArena::mousePressEvent(QMouseEvent *ev) {

    if(ev->type() == QEvent::MouseButtonPress)
    {

        QPoint p = ui->label->mapFrom(this, ev->pos());
        if(p.x() > 640 || p.y()> 480)
            return;

        switch (posEditada) {
        case 0:
            setPositionLeftUpper(p.x(), p.y());
            break;
        case 1:
            setPositionRightUpper(p.x(), p.y());
            break;
        case 2:
            setPositionRightLower(p.x(), p.y());
            break;
        case 3:
            setPositionLeftLower(p.x(), p.y());
            break;

        default:
            break;
        }
    }

}

CalibracaoArena::~CalibracaoArena()
{
//    QObject::disconnect(colorManagementThread, SIGNAL(newFrame(QImage)), this, SLOT(updateFrame(QImage)));

    delete calibracaoArenaThread;
    delete ui;
}
void CalibracaoArena::on_CalibracaoArena_finished(int result) {

}

void CalibracaoArena::reject() {

    stopThread();
    std::cout << "Tentando interromper CalibracaoArenaThread..." << std::endl;
    calibracaoArenaThread->quit();
    bool v = calibracaoArenaThread->wait(5000);
    if(v) {
        std::cout << "calibracaoArenaThread finalizada com sucesso..." << std::endl;
    } else {
        std::cout << "calibracaoArenaThread não finalizada..." << std::endl;
    }
    pauseProcessingThread(false);
    QDialog::reject();
}

void CalibracaoArena::setPositionLeftUpper(int x, int y) {
    ui->lineEdit->setText(QString::fromStdString(std::to_string(x)));
    ui->lineEdit_2->setText(QString::fromStdString(std::to_string(y)));
}

cv::Scalar CalibracaoArena::getPositionLeftUpper() {
    cv::Scalar v;
    v[0] = ui->lineEdit->text().toInt();
    v[1] = ui->lineEdit_2->text().toInt();
    return v;
}

void CalibracaoArena::setPositionRightUpper(int x, int y) {
    ui->lineEdit_3->setText(QString::fromStdString(std::to_string(x)));
    ui->lineEdit_4->setText(QString::fromStdString(std::to_string(y)));
}

cv::Scalar CalibracaoArena::getPositionRightUpper() {
    cv::Scalar v;
    v[0] = ui->lineEdit_3->text().toInt();
    v[1] = ui->lineEdit_4->text().toInt();
    return v;
}

void CalibracaoArena::setPositionRightLower(int x, int y) {
    ui->lineEdit_5->setText(QString::fromStdString(std::to_string(x)));
    ui->lineEdit_6->setText(QString::fromStdString(std::to_string(y)));
}

cv::Scalar CalibracaoArena::getPositionRightLower() {
    cv::Scalar v;
    v[0] = ui->lineEdit_5->text().toInt();
    v[1] = ui->lineEdit_6->text().toInt();
    return v;
}

void CalibracaoArena::setPositionLeftLower(int x, int y) {
    ui->lineEdit_7->setText(QString::fromStdString(std::to_string(x)));
    ui->lineEdit_8->setText(QString::fromStdString(std::to_string(y)));
}

cv::Scalar CalibracaoArena::getPositionLeftLower() {
    cv::Scalar v;
    v[0] = ui->lineEdit_7->text().toInt();
    v[1] = ui->lineEdit_8->text().toInt();
    return v;
}

void CalibracaoArena::setFromConfig() {
    Configuracao &conf = Configuracao::getInstance();
    cv::Scalar posLL = conf.getPositionLowerLeft();
    setPositionLeftLower(posLL[0], posLL[1]);

    cv::Scalar posRL = conf.getPositionLowerRight();
    setPositionRightLower(posRL[0], posRL[1]);

    cv::Scalar posLU = conf.getPositionUpperLeft();
    setPositionLeftUpper(posLU[0], posLU[1]);

    cv::Scalar posRU = conf.getPositionUpperRight();
    setPositionRightUpper(posRU[0], posRU[1]);
}

void CalibracaoArena::setLabels(int n) {
    ui->pushButton->setText("Calibrar");
    ui->pushButton_2->setText("Calibrar");
    ui->pushButton_3->setText("Calibrar");
    ui->pushButton_4->setText("Calibrar");

    switch(n) {
    case 0:
        ui->pushButton->setText("Calibrando");
        break;
    case 1:
        ui->pushButton_2->setText("Calibrando");
        break;
    case 2:
        ui->pushButton_3->setText("Calibrando");
        break;
    case 3:
        ui->pushButton_4->setText("Calibrando");
        break;
    default:
        break;
    }
}

void CalibracaoArena::on_pushButton_clicked() {
    if(posEditada == 0) {
        posEditada = -1;
    } else {
        posEditada = 0;
    }
    setLabels(posEditada);
}

void CalibracaoArena::on_pushButton_2_clicked() {
    if(posEditada == 1) {
        posEditada = -1;
    } else {
        posEditada = 1;
    }
    setLabels(posEditada);
}

void CalibracaoArena::on_pushButton_3_clicked() {
    if(posEditada == 2) {
        posEditada = -1;
    } else {
        posEditada = 2;
    }
    setLabels(posEditada);
}

void CalibracaoArena::on_pushButton_4_clicked() {
    if(posEditada == 3) {
        posEditada = -1;
    } else {
        posEditada = 3;
    }
    setLabels(posEditada);
}

void CalibracaoArena::on_aplicar_clicked() {
    Configuracao &conf = Configuracao::getInstance();

    cv::Scalar v = getPositionLeftLower();
    conf.setPositionLowerLeft(v[0], v[1]);

    v = getPositionRightLower();
    conf.setPositionLowerRight(v[0], v[1]);

    v = getPositionLeftUpper();
    conf.setPositionUpperLeft(v[0], v[1]);

    v = getPositionRightUpper();
    conf.setPositionUpperRight(v[0], v[1]);

    updateBorders();
}
