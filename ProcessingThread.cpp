#include "ProcessingThread.h"

using namespace cv;
using namespace std;

bool corTime;//true para azul, False para amarelo

ProcessingThread::ProcessingThread(Buffer<cv::Mat> *buffer, Buffer<World> *bufferWorld, Buffer<cv::Mat> *bufferImagemProcessada)
    : paused(false) {
    this->buffer = buffer;
    this->bufferWorld = bufferWorld;
    this->bufferImagemProcessada = bufferImagemProcessada;
}

void ProcessingThread::run() {
    Configuracao& conf = Configuracao::getInstance();

    while(1) {

        {
            QMutexLocker locker(&m_mutex);
            if(paused) {
                continue;
            }
        }

        Mat frame = buffer->get();

        if(conf.getBlueLowerBound() == NULL || conf.getBlueUpperBound() == NULL
                || conf.getOrangeLowerBound() == NULL || conf.getOrangeUpperBound() == NULL
                || conf.getColor1LowerBound() == NULL || conf.getColor1UpperBound() == NULL
                || conf.getColor2LowerBound() == NULL || conf.getColor2UpperBound() == NULL
                || conf.getColor3LowerBound() == NULL || conf.getColor3UpperBound() == NULL) {

            bufferImagemProcessada->add(frame);
            continue;
        }


        Mat frameHsv;
        cvtColor(frame, frameHsv ,CV_BGR2HSV);
        BlobProcessor *teamColorBlobProcessor;
        if(corTime){
            teamColorBlobProcessor = new BlobProcessor(frameHsv, *conf.getBlueLowerBound(), *conf.getBlueUpperBound());
            teamColorBlobProcessor->process(3);
        } else {
            teamColorBlobProcessor = new BlobProcessor(frameHsv, *conf.getYellowLowerBound(), *conf.getYellowUpperBound());
            teamColorBlobProcessor->process(3);
        }

        BlobProcessor ballColorBlobProcessor(frameHsv, *conf.getOrangeLowerBound(), *conf.getOrangeUpperBound());
        ballColorBlobProcessor.processBall(1);

        BlobProcessor color1BlobProcessor(frameHsv, *conf.getColor1LowerBound(), *conf.getColor1UpperBound());
        color1BlobProcessor.process(1);

        BlobProcessor color2BlobProcessor(frameHsv, *conf.getColor2LowerBound(), *conf.getColor2UpperBound());
        color2BlobProcessor.process(1);

        BlobProcessor color3BlobProcessor(frameHsv, *conf.getColor3LowerBound(), *conf.getColor3UpperBound());
        color3BlobProcessor.process(1);

        // mostra azul
//        for(list<Scalar>::iterator it = teamColorBlobProcessor.getResults().begin(); it != teamColorBlobProcessor.getResults().end(); it++) {
//            Scalar centro = *it;
//            Point point(centro[0], centro[1]);
//            cv::circle(frame, point, 4, Scalar(168., 165., 122.), 4);
//        }

        // mostra jogador azul
        //Scalar centro1 = teamColorBlobProcessor.getResults().front();
//        Point point1(centro1[0], centro1[1]);
//        cv::circle(frame, point1, 4, Scalar(112, 160, 128), 4);

//        // mostra jogador cor 1
        Scalar centro1_aux = color1BlobProcessor.getResults().front();
//        Point point1(centro1[0], centro1[1]);
//        cv::circle(frame, point1, 4, Scalar(112, 160, 128), 4);

        // mostra jogador cor 2
        Scalar centro2_aux = color2BlobProcessor.getResults().front();
        //Point point2(centro1[0], centro1[1]);
        //cv::circle(frame, point2, 4, Scalar(112, 160, 128), 4);

        // mostra jogador cor 3
        Scalar centro3_aux = color3BlobProcessor.getResults().front();
//        Point point3(centro3[0], centro3[1]);
//        cv::circle(frame, point3, 4, Scalar(255, 0, 0), 4);
        list<Scalar> listaTime = teamColorBlobProcessor->getResults();
//        cout << listaTime.size() << endl;

        Scalar centro1 = Scalar(0,0,0);
        double menorDist = 100000;
        for(list<Scalar>::iterator it = listaTime.begin(); it != listaTime.end(); it++) // pegar somente os blobs que estão pertos
        {

            if(((centro1_aux[0] - (*it)[0])*(centro1_aux[0] - (*it)[0]) + (centro1_aux[1] - (*it)[1])*(centro1_aux[1] - (*it)[1])) < menorDist)
            {
                menorDist = (centro1_aux[0] - (*it)[0])*(centro1_aux[0] - (*it)[0]) + (centro1_aux[1] - (*it)[1])*(centro1_aux[1] - (*it)[1]);
                centro1 = *it;
            }

        }

        Scalar centro2 = Scalar(0,0,0);
        menorDist = 100000;
        for(list<Scalar>::iterator it = listaTime.begin(); it != listaTime.end(); it++) // pegar somente os blobs que estão pertos
        {
            if(((centro2_aux[0] - (*it)[0])*(centro2_aux[0] - (*it)[0]) + (centro2_aux[1] - (*it)[1])*(centro2_aux[1] - (*it)[1])) < menorDist)
            {
                menorDist = (centro2_aux[0] - (*it)[0])*(centro2_aux[0] - (*it)[0]) + (centro2_aux[1] - (*it)[1])*(centro2_aux[1] - (*it)[1]);
                centro2 = *it;
            }
        }

        Scalar centro3 = Scalar(0,0,0);
        menorDist = 100000;
        for(list<Scalar>::iterator it = listaTime.begin(); it != listaTime.end(); it++) // pegar somente os blobs que estão pertos
        {
            if(((centro3_aux[0] - (*it)[0])*(centro3_aux[0] - (*it)[0]) + (centro3_aux[1] - (*it)[1])*(centro3_aux[1] - (*it)[1])) < menorDist)
            {
                menorDist = (centro3_aux[0] - (*it)[0])*(centro3_aux[0] - (*it)[0]) + (centro3_aux[1] - (*it)[1])*(centro3_aux[1] - (*it)[1]);
                centro3 = *it;
            }
        }

        // mostra bola
        Scalar centroBola = ballColorBlobProcessor.getResults().front();
//        Point point4(centroBola[0], centroBola[1]);
//        cv::circle(frame, point4, 4, Scalar(112, 160, 128), 4);
        Player aux1 = Player(centro1[0],centro1[1], centro1_aux[0], centro1_aux[1]);
        Player aux2 = Player(centro2[0],centro2[1], centro2_aux[0], centro2_aux[1]);
        Player aux3 = Player(centro3[0], centro3[1], centro3_aux[0], centro3_aux[1]);
        Player teammates[] = {aux1, aux2, aux3};
        Ball ball(centroBola[0], centroBola[1]);

        World world;
        world.setTeammates(teammates);
        world.setBall(ball);

        bufferWorld->add(world);
        bufferImagemProcessada->add(frame);
        delete(teamColorBlobProcessor);
    }
}

void ProcessingThread::pause(bool b) {
    QMutexLocker locker(&m_mutex);
    paused = b;
}

void ProcessingThread::escolheCor(bool cor){
    corTime = cor;
}
