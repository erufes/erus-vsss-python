#include "ColorManagement.h"
#include "ui_ColorManagement.h"
#include "Configuracao.h"
#include "Utils.h"

#include <QMouseEvent>
#include <iostream>

ColorManagement::ColorManagement(Buffer<cv::Mat> *buffer, QWidget *parent) :
    QDialog(parent),
    ui(new Ui::ColorManagement), showFilter(false), corEditada(0)
{
    ui->setupUi(this);
    setModal(true);

    colorManagementThread = new ColorManagementThread(buffer);
    qRegisterMetaType< cv::Mat >("cv::Mat");
    QObject::connect(colorManagementThread, SIGNAL(newFrame(cv::Mat)), this, SLOT(updateFrame(cv::Mat)));
    QObject::connect(this, SIGNAL(stopThread()), colorManagementThread, SLOT(stop()));
    colorManagementThread->start();

    preencheCampos();
}

void ColorManagement::mousePressEvent(QMouseEvent *ev) {

    if(ev->type() == QEvent::MouseButtonPress) {

        // Nenhuma cor sendo editada
        if(corEditada == 0) {
            return;
        }

        QPoint p = ui->label->mapFrom(this, ev->pos());

        const int x = p.x();
        const int y = p.y();
        // Ponto alem da imagem
        if(x > 640 || y > 480) {
            return;
        }
        Configuracao &conf = Configuracao::getInstance();
        if(conf.getStateCalibracao()){
            if(first_click){
                std::cout << "dentro" << p.x() << p.y()  << std::endl;
                old_pos[0] = p.x();
                old_pos[1] = p.y();
                first_click = !first_click;
                return;
            }
            first_click = !first_click;
            std::cout << "fora" << p.x() << p.y()  << std::endl;
            if(old_pos[0] < x && old_pos[1] < y)
            {
                cv::Mat hsvImage;
                cv::cvtColor(frame, hsvImage, CV_BGR2HSV);
                for(int i = old_pos[0]; i < x ; i++)
                    for(int j = old_pos[1] ; j < y ; j++)
                    {

                        cv::Vec3b color = hsvImage.at<cv::Vec3b>(cv::Point(i, j));

                        //std::cout << color << std::endl;

                        cv::Vec3b oldLower = pegaCorLower(corEditada);
                        cv::Vec3b oldUpper = pegaCorUpper(corEditada);
                        alteraLimitesCor(corEditada, oldLower, oldUpper, color);
                    }
            }
            else return;
    }
    else{
            cv::Mat hsvImage;
            cv::cvtColor(frame, hsvImage, CV_BGR2HSV);
            cv::Vec3b color = hsvImage.at<cv::Vec3b>(cv::Point(p.x(), p.y()));
            cv::Vec3b oldLower = pegaCorLower(corEditada);
            cv::Vec3b oldUpper = pegaCorUpper(corEditada);
            alteraLimitesCor(corEditada, oldLower, oldUpper, color);
        }

    }
}

cv::Vec3b ColorManagement::pegaCorLower(int n) {
    cv::Vec3b color;

    switch(n) {
    case 1:
        color[0] = ui->corAzulLowerH->text().toInt();
        color[1] = ui->corAzulLowerS->text().toInt();
        color[2] = ui->corAzulLowerV->text().toInt();
        break;
    case 2:
        color[0] = ui->corAmareloLowerH->text().toInt();
        color[1] = ui->corAmareloLowerS->text().toInt();
        color[2] = ui->corAmareloLowerV->text().toInt();
        break;
    case 3:
        color[0] = ui->corLaranjaLowerH->text().toInt();
        color[1] = ui->corLaranjaLowerS->text().toInt();
        color[2] = ui->corLaranjaLowerV->text().toInt();
        break;
    case 4:
        color[0] = ui->cor1LowerH->text().toInt();
        color[1] = ui->cor1LowerS->text().toInt();
        color[2] = ui->cor1LowerV->text().toInt();
        break;
    case 5:
        color[0] = ui->cor2LowerH->text().toInt();
        color[1] = ui->cor2LowerS->text().toInt();
        color[2] = ui->cor2LowerV->text().toInt();
        break;
    case 6:
        color[0] = ui->cor3LowerH->text().toInt();
        color[1] = ui->cor3LowerS->text().toInt();
        color[2] = ui->cor3LowerV->text().toInt();
        break;
    case 7:
        color[0] = ui->corEnemyLowerH->text().toInt();
        color[1] = ui->corEnemyLowerS->text().toInt();
        color[2] = ui->corEnemyLowerV->text().toInt();
        break;
    default:
        color[0] = 0;
        color[1] = 0;
        color[2] = 0;
    }

    return color;
}

cv::Vec3b ColorManagement::pegaCorUpper(int n) {
    cv::Vec3b color;

    switch(n) {
    case 1:
        color[0] = ui->corAzulUpperH->text().toInt();
        color[1] = ui->corAzulUpperS->text().toInt();
        color[2] = ui->corAzulUpperV->text().toInt();
        break;
    case 2:
        color[0] = ui->corAmareloUpperH->text().toInt();
        color[1] = ui->corAmareloUpperS->text().toInt();
        color[2] = ui->corAmareloUpperV->text().toInt();
        break;
    case 3:
        color[0] = ui->corLaranjaUpperH->text().toInt();
        color[1] = ui->corLaranjaUpperS->text().toInt();
        color[2] = ui->corLaranjaUpperV->text().toInt();
        break;
    case 4:
        color[0] = ui->cor1UpperH->text().toInt();
        color[1] = ui->cor1UpperS->text().toInt();
        color[2] = ui->cor1UpperV->text().toInt();
        break;
    case 5:
        color[0] = ui->cor2UpperH->text().toInt();
        color[1] = ui->cor2UpperS->text().toInt();
        color[2] = ui->cor2UpperV->text().toInt();
        break;
    case 6:
        color[0] = ui->cor3UpperH->text().toInt();
        color[1] = ui->cor3UpperS->text().toInt();
        color[2] = ui->cor3UpperV->text().toInt();
        break;
    case 7:
        color[0] = ui->corEnemyUpperH->text().toInt();
        color[1] = ui->corEnemyUpperS->text().toInt();
        color[2] = ui->corEnemyUpperV->text().toInt();
        break;
    default:
        color[0] = 0;
        color[1] = 0;
        color[2] = 0;
    }

    return color;
}

void ColorManagement::alteraLimitesCor(int n, cv::Vec3b lower, cv::Vec3b upper, cv::Vec3b color) {
    // n=3 -> LARANJA
    if(n == 3) {
        if(color[0] < 90) {
            if (color[0] > lower[0]) {
                lower[0] = color[0];
            }
        } else {
            if (color[0] < upper[0]) {
                upper[0] = color[0];
            }
        }
    } else {
        if (color[0] < lower[0]) {
            lower[0] = color[0];
        }

        if (color[0] > upper[0]) {
            upper[0] = color[0];
        }
    }

    if (color[1] < lower[1]) {
        lower[1] = color[1];
    }
    if (color[2] < lower[2]) {
        lower[2] = color[2];
    }

    if (color[1] > upper[1]) {
        upper[1] = color[1];
    }
    if (color[2] > upper[2]) {
        upper[2] = color[2];
    }

    setaCorLower(n, lower);
    setaCorUpper(n, upper);
}

void ColorManagement::setaCorLower(int n, cv::Vec3b color) {
    switch(n) {
    case 1:
        ui->corAzulLowerH->setText(QString::number(color[0]));
        ui->corAzulLowerS->setText(QString::number(color[1]));
        ui->corAzulLowerV->setText(QString::number(color[2]));
        break;
    case 2:
        ui->corAmareloLowerH->setText(QString::number(color[0]));
        ui->corAmareloLowerS->setText(QString::number(color[1]));
        ui->corAmareloLowerV->setText(QString::number(color[2]));
        break;
    case 3:
        ui->corLaranjaLowerH->setText(QString::number(color[0]));
        ui->corLaranjaLowerS->setText(QString::number(color[1]));
        ui->corLaranjaLowerV->setText(QString::number(color[2]));
        break;
    case 4:
        ui->cor1LowerH->setText(QString::number(color[0]));
        ui->cor1LowerS->setText(QString::number(color[1]));
        ui->cor1LowerV->setText(QString::number(color[2]));
        break;
    case 5:
        ui->cor2LowerH->setText(QString::number(color[0]));
        ui->cor2LowerS->setText(QString::number(color[1]));
        ui->cor2LowerV->setText(QString::number(color[2]));
        break;
    case 6:
        ui->cor3LowerH->setText(QString::number(color[0]));
        ui->cor3LowerS->setText(QString::number(color[1]));
        ui->cor3LowerV->setText(QString::number(color[2]));
        break;
    case 7:
        ui->corEnemyLowerH->setText(QString::number(color[0]));
        ui->corEnemyLowerS->setText(QString::number(color[1]));
        ui->corEnemyLowerV->setText(QString::number(color[2]));
        break;
    }
}

void ColorManagement::setaCorUpper(int n, cv::Vec3b color) {
    switch(n) {
    case 1:
        ui->corAzulUpperH->setText(QString::number(color[0]));
        ui->corAzulUpperS->setText(QString::number(color[1]));
        ui->corAzulUpperV->setText(QString::number(color[2]));
        break;
    case 2:
        ui->corAmareloUpperH->setText(QString::number(color[0]));
        ui->corAmareloUpperS->setText(QString::number(color[1]));
        ui->corAmareloUpperV->setText(QString::number(color[2]));
        break;
    case 3:
        ui->corLaranjaUpperH->setText(QString::number(color[0]));
        ui->corLaranjaUpperS->setText(QString::number(color[1]));
        ui->corLaranjaUpperV->setText(QString::number(color[2]));
        break;
    case 4:
        ui->cor1UpperH->setText(QString::number(color[0]));
        ui->cor1UpperS->setText(QString::number(color[1]));
        ui->cor1UpperV->setText(QString::number(color[2]));
        break;
    case 5:
        ui->cor2UpperH->setText(QString::number(color[0]));
        ui->cor2UpperS->setText(QString::number(color[1]));
        ui->cor2UpperV->setText(QString::number(color[2]));
        break;
    case 6:
        ui->cor3UpperH->setText(QString::number(color[0]));
        ui->cor3UpperS->setText(QString::number(color[1]));
        ui->cor3UpperV->setText(QString::number(color[2]));
        break;
    case 7:
        ui->corEnemyUpperH->setText(QString::number(color[0]));
        ui->corEnemyUpperS->setText(QString::number(color[1]));
        ui->corEnemyUpperV->setText(QString::number(color[2]));
        break;
    }
}

ColorManagement::~ColorManagement()
{
//    QObject::disconnect(colorManagementThread, SIGNAL(newFrame(QImage)), this, SLOT(updateFrame(QImage)));

    delete colorManagementThread;
    delete ui;
}

void ColorManagement::updateFrame(const cv::Mat &frame) {
    this->frame = frame;

//    cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(3,3));

    cv::Mat imageToShow;
    if(showFilter && corEditada!=0) {
        cv::Mat hsvImage;
        cv::cvtColor(frame, hsvImage, CV_BGR2HSV);

//        cv::Mat kernel = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(3, 3));
//        cv::morphologyEx(hsvImage, hsvImage, cv::MORPH_CLOSE, kernel);
//        cv::morphologyEx(hsvImage, hsvImage, cv::MORPH_OPEN, kernel);

//        cv::GaussianBlur(hsvImage, hsvImage, cv::Size(9, 9), 2, 2);

        cv::Vec3b lower = pegaCorLower(corEditada);
        cv::Vec3b upper = pegaCorUpper(corEditada);

        if(corEditada == 3) {
            std::cout << "teste" << std::endl;
            cv::Mat maskRange1, maskRange2;

            cv::Scalar lowerRange1(0, lower[1], lower[2]), upperRange1(lower[0], upper[1], upper[2]);
            cv::inRange(hsvImage, lowerRange1, upperRange1, maskRange1);

            cv::Scalar lowerRange2(upper[0], lower[1], lower[2]), upperRange2(255, upper[1], upper[2]);
            cv::inRange(hsvImage, lowerRange2, upperRange2, maskRange2);

            cv::addWeighted(maskRange1, 1, maskRange2, 1, 0, imageToShow);
        } else {
                cv::inRange(hsvImage, lower, upper, imageToShow);
            if(corEditada == 7)
                imageToShow = 255 - imageToShow;

        }
    } else {
        imageToShow = frame;
    }
    QImage drawableImage = Utils::cvMatToQImage(imageToShow);
    ui->label->setPixmap(QPixmap::fromImage(drawableImage));
}


void ColorManagement::on_ColorManagement_finished(int result) {

}

void ColorManagement::reject() {

    stopThread();
    std::cout << "Tentando interromper colorManagementThread..." << std::endl;
    colorManagementThread->quit();
    bool v = colorManagementThread->wait(5000);
    if(v) {
        std::cout << "colorManagementThread finalizada com sucesso..." << std::endl;
    } else {
        std::cout << "colorManagementThread não finalizada..." << std::endl;
    }
    pauseProcessingThread(false);
    QDialog::reject();
}

void ColorManagement::preencheCampos() {
    Configuracao& conf = Configuracao::getInstance();

    if(conf.getBlueLowerBound() != NULL) {
        cv::Scalar *blueLowerBound = conf.getBlueLowerBound();
        ui->corAzulLowerH->setText(QString::number(blueLowerBound->val[0]));
        ui->corAzulLowerS->setText(QString::number(blueLowerBound->val[1]));
        ui->corAzulLowerV->setText(QString::number(blueLowerBound->val[2]));
    } else {
        ui->corAzulLowerH->setText("255");
        ui->corAzulLowerS->setText("255");
        ui->corAzulLowerV->setText("255");
    }

    if(conf.getBlueUpperBound() != NULL) {
        cv::Scalar *blueUpperBound = conf.getBlueUpperBound();
        ui->corAzulUpperH->setText(QString::number(blueUpperBound->val[0]));
        ui->corAzulUpperS->setText(QString::number(blueUpperBound->val[1]));
        ui->corAzulUpperV->setText(QString::number(blueUpperBound->val[2]));
    } else {
        ui->corAzulUpperH->setText("0");
        ui->corAzulUpperS->setText("0");
        ui->corAzulUpperV->setText("0");
    }

    if(conf.getEnemyLowerBound() != NULL) {
        cv::Scalar *enemyLowerBound = conf.getEnemyLowerBound();
        ui->corEnemyLowerH->setText(QString::number(enemyLowerBound->val[0]));
        ui->corEnemyLowerS->setText(QString::number(enemyLowerBound->val[1]));
        ui->corEnemyLowerV->setText(QString::number(enemyLowerBound->val[2]));
    } else {
        ui->corEnemyLowerH->setText("255");
        ui->corEnemyLowerS->setText("255");
        ui->corEnemyLowerV->setText("255");
    }
    if(conf.getEnemyUpperBound() != NULL) {
        cv::Scalar *enemyUpperBound = conf.getEnemyUpperBound();
        ui->corEnemyUpperH->setText(QString::number(enemyUpperBound->val[0]));
        ui->corEnemyUpperS->setText(QString::number(enemyUpperBound->val[1]));
        ui->corEnemyUpperV->setText(QString::number(enemyUpperBound->val[2]));
    } else {
        ui->corEnemyUpperH->setText("0");
        ui->corEnemyUpperS->setText("0");
        ui->corEnemyUpperV->setText("0");
    }
    if(conf.getYellowLowerBound() != NULL) {
        cv::Scalar *yellowLowerBound = conf.getYellowLowerBound();
        ui->corAmareloLowerH->setText(QString::number(yellowLowerBound->val[0]));
        ui->corAmareloLowerS->setText(QString::number(yellowLowerBound->val[1]));
        ui->corAmareloLowerV->setText(QString::number(yellowLowerBound->val[2]));
    } else {
        ui->corAmareloLowerH->setText("255");
        ui->corAmareloLowerS->setText("255");
        ui->corAmareloLowerV->setText("255");
    }

    if(conf.getYellowUpperBound() != NULL) {
        cv::Scalar *yellowUpperBound = conf.getYellowUpperBound();
        ui->corAmareloUpperH->setText(QString::number(yellowUpperBound->val[0]));
        ui->corAmareloUpperS->setText(QString::number(yellowUpperBound->val[1]));
        ui->corAmareloUpperV->setText(QString::number(yellowUpperBound->val[2]));
    } else {
        ui->corAmareloUpperH->setText("0");
        ui->corAmareloUpperS->setText("0");
        ui->corAmareloUpperV->setText("0");
    }


    if(conf.getOrangeLowerBound() != NULL) {
        cv::Scalar *orangeLowerBound = conf.getOrangeLowerBound();
        ui->corLaranjaLowerH->setText(QString::number(orangeLowerBound->val[0]));
        ui->corLaranjaLowerS->setText(QString::number(orangeLowerBound->val[1]));
        ui->corLaranjaLowerV->setText(QString::number(orangeLowerBound->val[2]));
    } else {
        ui->corLaranjaLowerH->setText("255");
        ui->corLaranjaLowerS->setText("255");
        ui->corLaranjaLowerV->setText("255");
    }

    if(conf.getOrangeUpperBound() != NULL) {
        cv::Scalar *orangeUpperBound = conf.getOrangeUpperBound();
        ui->corLaranjaUpperH->setText(QString::number(orangeUpperBound->val[0]));
        ui->corLaranjaUpperS->setText(QString::number(orangeUpperBound->val[1]));
        ui->corLaranjaUpperV->setText(QString::number(orangeUpperBound->val[2]));
    } else {
        ui->corLaranjaUpperH->setText("0");
        ui->corLaranjaUpperS->setText("0");
        ui->corLaranjaUpperV->setText("0");
    }


    if(conf.getColor1LowerBound() != NULL) {
        cv::Scalar *cor1LowerBound = conf.getColor1LowerBound();
        ui->cor1LowerH->setText(QString::number(cor1LowerBound->val[0]));
        ui->cor1LowerS->setText(QString::number(cor1LowerBound->val[1]));
        ui->cor1LowerV->setText(QString::number(cor1LowerBound->val[2]));
    } else {
        ui->cor1LowerH->setText("255");
        ui->cor1LowerS->setText("255");
        ui->cor1LowerV->setText("255");
    }

    if(conf.getColor1UpperBound() != NULL) {
        cv::Scalar *cor1UpperBound = conf.getColor1UpperBound();
        ui->cor1UpperH->setText(QString::number(cor1UpperBound->val[0]));
        ui->cor1UpperS->setText(QString::number(cor1UpperBound->val[1]));
        ui->cor1UpperV->setText(QString::number(cor1UpperBound->val[2]));
    } else {
        ui->cor1UpperH->setText("0");
        ui->cor1UpperS->setText("0");
        ui->cor1UpperV->setText("0");
    }


    if(conf.getColor2LowerBound() != NULL) {
        cv::Scalar *cor2LowerBound = conf.getColor2LowerBound();
        ui->cor2LowerH->setText(QString::number(cor2LowerBound->val[0]));
        ui->cor2LowerS->setText(QString::number(cor2LowerBound->val[1]));
        ui->cor2LowerV->setText(QString::number(cor2LowerBound->val[2]));
    } else {
        ui->cor2LowerH->setText("255");
        ui->cor2LowerS->setText("255");
        ui->cor2LowerV->setText("255");
    }

    if(conf.getColor2UpperBound() != NULL) {
        cv::Scalar *cor2UpperBound = conf.getColor2UpperBound();
        ui->cor2UpperH->setText(QString::number(cor2UpperBound->val[0]));
        ui->cor2UpperS->setText(QString::number(cor2UpperBound->val[1]));
        ui->cor2UpperV->setText(QString::number(cor2UpperBound->val[2]));
    } else {
        ui->cor2UpperH->setText("0");
        ui->cor2UpperS->setText("0");
        ui->cor2UpperV->setText("0");
    }


    if(conf.getColor3LowerBound() != NULL) {
        cv::Scalar *cor3LowerBound = conf.getColor3LowerBound();
        ui->cor3LowerH->setText(QString::number(cor3LowerBound->val[0]));
        ui->cor3LowerS->setText(QString::number(cor3LowerBound->val[1]));
        ui->cor3LowerV->setText(QString::number(cor3LowerBound->val[2]));
    } else {
        ui->cor3LowerH->setText("255");
        ui->cor3LowerS->setText("255");
        ui->cor3LowerV->setText("255");
    }

    if(conf.getColor3UpperBound() != NULL) {
        cv::Scalar *cor3UpperBound = conf.getColor3UpperBound();
        ui->cor3UpperH->setText(QString::number(cor3UpperBound->val[0]));
        ui->cor3UpperS->setText(QString::number(cor3UpperBound->val[1]));
        ui->cor3UpperV->setText(QString::number(cor3UpperBound->val[2]));
    } else {
        ui->cor3UpperH->setText("0");
        ui->cor3UpperS->setText("0");
        ui->cor3UpperV->setText("0");
    }
}

void ColorManagement::setLabels(int n) {
    ui->pushButtonEnemy->setText("Calibrar");
    ui->pushButtonAzul->setText("Calibrar");
    ui->pushButtonAmarelo->setText("Calibrar");
    ui->pushButtonLaranja->setText("Calibrar");
    ui->pushButtonCor1->setText("Calibrar");
    ui->pushButtonCor2->setText("Calibrar");
    ui->pushButtonCor3->setText("Calibrar");

    switch(n) {
    case 1:
        ui->pushButtonAzul->setText("Calibrando");
        break;
    case 2:
        ui->pushButtonAmarelo->setText("Calibrando");
        break;
    case 3:
        ui->pushButtonLaranja->setText("Calibrando");
        break;
    case 4:
        ui->pushButtonCor1->setText("Calibrando");
        break;
    case 5:
        ui->pushButtonCor2->setText("Calibrando");
        break;
    case 6:
        ui->pushButtonCor3->setText("Calibrando");
        break;
    case 7:
        ui->pushButtonEnemy->setText("Calibrando");
        break;
    default:
        break;
    }
}

void ColorManagement::on_pushButtonAzul_clicked() {
    if(corEditada == 1) {
        corEditada = 0;
    } else {
        corEditada = 1;
    }
    setLabels(corEditada);
}

void ColorManagement::on_pushButtonAmarelo_clicked() {
    if(corEditada == 2) {
        corEditada = 0;
    } else {
        corEditada = 2;
    }
    setLabels(corEditada);
}

void ColorManagement::on_pushButtonLaranja_clicked() {
    if(corEditada == 3) {
        corEditada = 0;
    } else {
        corEditada = 3;
    }
    setLabels(corEditada);
}

void ColorManagement::on_pushButtonCor1_clicked() {
    if(corEditada == 4) {
        corEditada = 0;
    } else {
        corEditada = 4;
    }
    setLabels(corEditada);
}

void ColorManagement::on_pushButtonCor2_clicked() {
    if(corEditada == 5) {
        corEditada = 0;
    } else {
        corEditada = 5;
    }
    setLabels(corEditada);
}

void ColorManagement::on_pushButtonCor3_clicked() {
    if(corEditada == 6) {
        corEditada = 0;
    } else {
        corEditada = 6;
    }
    setLabels(corEditada);
}


void ColorManagement::on_mostrarFiltroCheckBox_stateChanged(int state) {
    if(state == Qt::Unchecked) {
        showFilter = false;
    } else if(state == Qt::Checked) {
        showFilter = true;
    }
}

void ColorManagement::on_salvar_clicked() {
    Configuracao &conf = Configuracao::getInstance();

    cv::Vec3b cor;

    cor = pegaCorLower(1);
    conf.setBlueLowerBound(cv::Scalar(cor[0], cor[1], cor[2]));
    cor = pegaCorUpper(1);
    conf.setBlueUpperBound(cv::Scalar(cor[0], cor[1], cor[2]));

    cor = pegaCorLower(2);
    conf.setYellowLowerBound(cv::Scalar(cor[0], cor[1], cor[2]));
    cor = pegaCorUpper(2);
    conf.setYellowUpperBound(cv::Scalar(cor[0], cor[1], cor[2]));

    cor = pegaCorLower(3);
    conf.setOrangeLowerBound(cv::Scalar(cor[0], cor[1], cor[2]));
    cor = pegaCorUpper(3);
    conf.setOrangeUpperBound(cv::Scalar(cor[0], cor[1], cor[2]));

    cor = pegaCorLower(4);
    conf.setColor1LowerBound(cv::Scalar(cor[0], cor[1], cor[2]));
    cor = pegaCorUpper(4);
    conf.setColor1UpperBound(cv::Scalar(cor[0], cor[1], cor[2]));

    cor = pegaCorLower(5);
    conf.setColor2LowerBound(cv::Scalar(cor[0], cor[1], cor[2]));
    cor = pegaCorUpper(5);
    conf.setColor2UpperBound(cv::Scalar(cor[0], cor[1], cor[2]));

    cor = pegaCorLower(6);
    conf.setColor3LowerBound(cv::Scalar(cor[0], cor[1], cor[2]));
    cor = pegaCorUpper(6);
    conf.setColor3UpperBound(cv::Scalar(cor[0], cor[1], cor[2]));

    cor = pegaCorLower(7);
    conf.setEnemyLowerBound(cv::Scalar(cor[0], cor[1], cor[2]));
    cor = pegaCorUpper(7);
    conf.setEnemyUpperBound(cv::Scalar(cor[0], cor[1], cor[2]));
}

void ColorManagement::on_reset_clicked() {
    preencheCampos();
}

void ColorManagement::on_label_linkActivated(const QString &link)
{

}

void ColorManagement::on_Quadrado_clicked()
{
    Configuracao &conf = Configuracao::getInstance();
    conf.setStateCalibracao(true);
    ui->Quadrado->setText("Quadrado (ON)");
    ui->Click->setText("Click");
}

void ColorManagement::on_Click_clicked()
{
    Configuracao &conf = Configuracao::getInstance();
    conf.setStateCalibracao(false);
    ui->Click->setText("Click (ON)");
    ui->Quadrado->setText("Quadrado");
}

void ColorManagement::on_pushButtonEnemy_clicked()
{
    if(corEditada == 7) {
        corEditada = 0;
    } else {
        corEditada = 7;
    }
    setLabels(corEditada);
}
