

#include "PythonThread.h"
#include <iostream>

using namespace std;
bool firstPaused = true;
bool firstRun = false;
bool atualizaBordas = false;
int tipoPenalty = 0; //1 para ataque, 0 para defesa

PythonThread::PythonThread(Buffer<World> *bufferWorld, Buffer<cv::Mat> *bufferImagemProcessada)
{
    pyAPI = new PythonAPI("main");
    this->bufferWorld = bufferWorld;
    this->bufferImagemProcessada = bufferImagemProcessada;
    paused = true;
}

PythonThread::~PythonThread()
{

}

void PythonThread::run()
{

    int ponto[2] = {0,0};
    cv::Mat frame;
    World world;
    PyObject *tupla;
    PyObject *lista = PyList_New(0);

    while (1) {

        if(atualizaBordas) {
            pyAPI->callFunctionUpdateBorders();
            atualizaBordas = false;
        }
        if(paused) {
            if(firstPaused){
                pyAPI->callFunctionPause();
                firstPaused = false;
            }
        }


        // Caso em que a configuração das cores nao foi preenchida
        frame = bufferImagemProcessada->get();
        if(bufferWorld->isEmpty()) {
            QImage drawableImage = Utils::cvMatToQImage(frame);
            emit(newFrame(drawableImage));
            continue;
        }

        world = bufferWorld->get();

        world.print();

//        std::cout << "INICIO DOS PRINTS" << std::endl;

//        cv::Point point0(world.getTeammate(0).getX(), world.getTeammate(0).getY());
//        cv::circle(frame, point0, 4, cv::Scalar(112, 160, 128), 4);
//        std::cout << point0 << std::endl;

//        cv::Point point1(world.getTeammate(1).getX(), world.getTeammate(1).getY());
//        cv::circle(frame, point1, 4, cv::Scalar(0, 0, 255), 4);
//        std::cout << point1 << std::endl;

//        cv::Point point2(world.getTeammate(2).getX(), world.getTeammate(2).getY());
//        cv::circle(frame, point2, 4, cv::Scalar(0, 255, 0), 4);
//        std::cout << point2 << std::endl;

//        cv::Point pointB(world.getBall().getX(), world.getBall().getY());
//        cv::circle(frame, pointB, 4, cv::Scalar(255, 0, 0), 4);
//        std::cout << pointB << std::endl;


        //cout << "tam lista: " << PyList_GET_SIZE(lista) << endl;
        if(lista != NULL) {
            for(int i = 0; i < PyList_GET_SIZE(lista); i++) {
                tupla = PyList_GetItem(lista, i);

                long x, y, b, g, r, xf, yf;
                std::string s;
                x = PyInt_AsLong(PyTuple_GetItem(tupla,0));
                y = PyInt_AsLong(PyTuple_GetItem(tupla,1));
                b = PyInt_AsLong(PyTuple_GetItem(tupla,2));
                g = PyInt_AsLong(PyTuple_GetItem(tupla,3));
                r = PyInt_AsLong(PyTuple_GetItem(tupla,4));
                s =  PyString_AsString(PyTuple_GetItem(tupla,5));
                xf = PyInt_AsLong(PyTuple_GetItem(tupla,6));
                yf = PyInt_AsLong(PyTuple_GetItem(tupla,7));


                //cout << x << " " << y << " " << b << " " << g << " " << r << endl;

                cv::Point point(Utils::cmToPx(x), Utils::cmToPx(y));
                cv::circle(frame, point, 4, cv::Scalar(b, g, r), 4); // print das bolinhas marotas
                if(s != "bola")
                {
                    //std::cout << "bola = " << x << "y = "<< y <<  std::endl;
                    cv::line(frame, point, cv::Point(Utils::cmToPx(xf), Utils::cmToPx(yf)), cv::Scalar(b,g,r), 4);
                }
            }

            Py_DECREF(lista);
        }

        QImage drawableImage = Utils::cvMatToQImage(frame);
        emit(newFrame(drawableImage));

        world.toCm();

        if(firstRun){
            lista = pyAPI->callFunctionRun(&world, tipoPenalty, paused);
            firstRun = false;

        } else {
            lista = pyAPI->callFunctionRun(&world, 0, paused);
        }
    }
}

void PythonThread::pauseGame(bool ativa) {
    paused = ativa;
    firstPaused = ativa;
}

void PythonThread::inicioPenalty(int tipo) {
    if(paused){
        paused = false;
        firstRun = true;
        tipoPenalty = tipo;
    }
}

void PythonThread::updateBorders() {
    atualizaBordas = true;
}
void PythonThread::TeamColor(bool team)
{
   if(team)
   {
       std::cout << "team azul selecionado" << std::endl;
   }
   else{
       std::cout << "team amarelo selecionado" << std::endl;
   }
}
