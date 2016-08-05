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

        BlobProcessor EnemyColorBlobProcessor(frameHsv, *conf.getEnemyLowerBound(), *conf.getEnemyUpperBound());
        EnemyColorBlobProcessor.process(7);
        //std::cout << conf.getEnemyLowerBound() << std::endl << conf.getEnemyUpperBound() << std::endl << conf.getColor1UpperBound() << std::endl;

        BlobProcessor ballColorBlobProcessor(frameHsv, *conf.getOrangeLowerBound(), *conf.getOrangeUpperBound());
        ballColorBlobProcessor.processBall(1);

        BlobProcessor color1BlobProcessor(frameHsv, *conf.getColor1LowerBound(), *conf.getColor1UpperBound());
        color1BlobProcessor.process(2);

        BlobProcessor color2BlobProcessor(frameHsv, *conf.getColor2LowerBound(), *conf.getColor2UpperBound());
        color2BlobProcessor.process(2);

        BlobProcessor color3BlobProcessor(frameHsv, *conf.getColor3LowerBound(), *conf.getColor3UpperBound());
        color3BlobProcessor.process(2);



        list<Scalar> listaTime = teamColorBlobProcessor->getResults();

//        // mostra jogador cor 1
        list<Scalar> listaCor1 = color1BlobProcessor.getResults();
        double menorDist1 = 500000000;
        Scalar menorDist1ob;
//        cout << listaTime.size() << endl;
        for(list<Scalar>::iterator it = listaCor1.begin(); it != listaCor1.end(); it++) {
            Scalar blobColorido = *it;
            for(list<Scalar>::iterator it2 = listaTime.begin(); it2 != listaTime.end(); it2++) {
                Scalar blobTime = *it2;

                if(norma2(blobColorido, blobTime) < menorDist1) {
                    menorDist1ob = blobColorido;
                    menorDist1 = norma2(blobColorido, blobTime);
                }
            }
        }
        Scalar centro1_aux = menorDist1ob;


        // mostra jogador cor 2
        list<Scalar> listaCor2 = color2BlobProcessor.getResults();
        double menorDist2 = 500000000;
        Scalar menorDist2ob;
//        cout << listaTime.size() << endl;
        for(list<Scalar>::iterator it = listaCor2.begin(); it != listaCor2.end(); it++) {
            Scalar blobColorido = *it;
            for(list<Scalar>::iterator it2 = listaTime.begin(); it2 != listaTime.end(); it2++) {
                Scalar blobTime = *it2;

                if(norma2(blobColorido, blobTime) < menorDist2) {
                    menorDist2ob = blobColorido;
                    menorDist2 = norma2(blobColorido, blobTime);
                }
            }
        }

        Scalar centro2_aux = menorDist2ob;


        // mostra jogador cor 3

        list<Scalar> listaCor3 = color3BlobProcessor.getResults();
        double menorDist3 = 500000000;
        Scalar menorDist3ob;
//        cout << listaTime.size() << endl;
        for(list<Scalar>::iterator it = listaCor3.begin(); it != listaCor3.end(); it++) {
            Scalar blobColorido = *it;
            for(list<Scalar>::iterator it2 = listaTime.begin(); it2 != listaTime.end(); it2++) {
                Scalar blobTime = *it2;

                if(norma2(blobColorido, blobTime) < menorDist3) {
                    menorDist3ob = blobColorido;
                    menorDist3 = norma2(blobColorido, blobTime);
                }
            }
        }

        Scalar centro3_aux = menorDist3ob;



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

double ProcessingThread::norma2(Scalar a, Scalar b) {
    return Utils::pxToCm((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1]));
}

void ProcessingThread::pause(bool b) {
    QMutexLocker locker(&m_mutex);
    paused = b;
}

void ProcessingThread::escolheCor(bool cor){
    corTime = cor;
}

