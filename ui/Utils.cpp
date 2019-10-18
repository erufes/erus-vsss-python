#include "Utils.h"

float Utils::pxToCm(int px) {
    Configuracao& conf = Configuracao::getInstance();
    const float comprimentoCm = conf.getComprimentoArena();
    cv::Point p1 = cv::Point(conf.getPositionLowerLeft()[0], conf.getPositionLowerLeft()[1]);
    cv::Point p2 = cv::Point(conf.getPositionLowerRight()[0], conf.getPositionLowerRight()[1]);
    const float comprimentoPx = Utils::norm(p1, p2);
    //std::cout << "p1x " << conf.getPositionLowerLeft()[1] << " p1y " << p1.y << std::endl;
    //std::cout << "p2x " << p2.x << " p2y " << p2.y << std::endl;
    return px*(comprimentoCm/comprimentoPx);
}

float Utils::cmToPx(float cm) {
    Configuracao& conf = Configuracao::getInstance();
    const float comprimentoCm = conf.getComprimentoArena();
    cv::Point p1 = cv::Point(conf.getPositionLowerLeft()[0], conf.getPositionLowerLeft()[1]);
    cv::Point p2 = cv::Point(conf.getPositionLowerRight()[0], conf.getPositionLowerRight()[1]);
    //std::cout << p1.x << p2.x << std::endl;
    const float comprimentoPx = Utils::norm(p1, p2);

    return cm*(comprimentoPx/comprimentoCm);
}

float Utils::norm(cv::Point a, cv::Point b) {
    float x = a.x-b.x;
    float y = a.y-b.y;
    return sqrt(x * x + y * y);
}

QImage Utils::cvMatToQImage(const cv::Mat &inMat)
{
    switch (inMat.type())
    {
        // 8-bit, 4 channel
    case CV_8UC4:
    {
        QImage image(inMat.data, inMat.cols, inMat.rows, inMat.step, QImage::Format_RGB32);

        return image;
    }

        // 8-bit, 3 channel
    case CV_8UC3:
    {
        QImage image(inMat.data, inMat.cols, inMat.rows, inMat.step, QImage::Format_RGB888);

        return image.rgbSwapped();
    }

        // 8-bit, 1 channel
    case CV_8UC1:
    {
        static QVector<QRgb>  sColorTable;

        // only create our color table once
        if (sColorTable.isEmpty())
        {
            for (int i = 0; i < 256; ++i)
                sColorTable.push_back(qRgb(i, i, i));
        }

        QImage image(inMat.data, inMat.cols, inMat.rows, inMat.step, QImage::Format_Indexed8);

        image.setColorTable(sColorTable);

        return image;
    }

    default:
        qWarning() << "ASM::cvMatToQImage() - cv::Mat image type not handled in switch:" << inMat.type();
        break;
    }

    return QImage();
}
