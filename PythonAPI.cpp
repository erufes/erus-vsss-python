#include "PythonAPI.h"
#include <iostream>
#include <assert.h>
#include "Configuracao.h"
#include "Utils.h"
#include <algorithm>    // std::max

using namespace std;

PythonAPI::PythonAPI(const char *file)
{
    Py_Initialize();

    //Guilherme: Escolhe o caminho dos arquivos Python
    char dir[] = "C:\\Users\\Erus\\Documents\\verysmall\\scripts";
    PyObject* sysPath = PySys_GetObject("path");
    PyObject* curDir = PyString_FromString(dir);
    PyList_Append(sysPath, curDir);
    Py_DECREF(curDir);
    //Fim

    pName = PyString_FromString(file);
    /* Error checking of pName left out */

    pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (pModule == NULL){
        PyErr_Print();
        fprintf(stderr, "Failed to load \"%s\"\n", file);
    }
}

PythonAPI::~PythonAPI()
{
    Py_DECREF(pModule);
    Py_Finalize();

    //como chamar super??
}

PyObject* PythonAPI::callFunctionRun(double* args){
    PyObject *pFunc; //*pDict,
    PyObject *pArgs, *pValue;
    int nParametros = 13;
    pFunc = PyObject_GetAttrString(pModule, "run");
    /* pFunc is a new reference */

    if (pFunc && PyCallable_Check(pFunc)) {
        pArgs = PyTuple_New(nParametros);
        for (int i = 0; i < nParametros; ++i) {
            pValue = PyFloat_FromDouble(args[i]);
            if (!pValue) {
                Py_DECREF(pArgs);
                fprintf(stderr, "Cannot convert argument\n");
                return NULL;
            }
            /* pValue reference stolen here: */
            PyTuple_SetItem(pArgs, i, pValue);
        }
        pValue = PyObject_CallObject(pFunc, pArgs);
        Py_DECREF(pArgs);
        if (pValue != NULL) {
            //printf("Result of call: %ld\n", PyInt_AsLong(PyTuple_GetItem(pValue,1)));
//            retorno[0] = PyInt_AsLong(PyTuple_GetItem(pValue,0));
//            retorno[1] = PyInt_AsLong(PyTuple_GetItem(pValue,1));
//            retorno = pValue;
            //Py_DECREF(pValue);
        } else {
            Py_DECREF(pFunc);
            PyErr_Print();
            fprintf(stderr,"Call failed\n");
            return NULL;
        }
    }
    else {
        if (PyErr_Occurred())
            PyErr_Print();
        fprintf(stderr, "Cannot find function run \n");
    }
    Py_XDECREF(pFunc);
    return pValue;
}

PyObject *PythonAPI::callFunctionRun(World* world, int penalty, int paused){
//Falta modificar para escolher quando é penalty
    //static int cnt = 0;
    double args[13];
    //int parametros[] = {50, 50, 0, 70, 70, 3.1415, 100, 100, 0, 120, 120, 0};
    Player player;
    Ball ball = world->getBall();
    for(int i = 0; i < 3; i++) {
        player = world->getTeammate(i);
        args[3*i] = player.getX();
        args[3*i+1] = player.getY();
        args[3*i+2] = player.getAngle();
        //std::cout << player.getAngle() << " == " << args[3*i+2] << "?\n";
        //if( player.getAngle() != args[3*i+2] ){cnt++;} // Esta guardando rad float em int, pq?
        //assert ( cnt < 20 );
    }

    args[9] = ball.getX();
    args[10] = ball.getY();
    args[11] = penalty; //modificar para levar penalty em consideração
    args[12] = paused;

    return callFunctionRun(args);
}

int PythonAPI::callFunctionPause(){
    PyObject *pFunc; //,*pDict
    PyObject *pArgs, *pValue;
    //int nParametros = 15;
    pFunc = PyObject_GetAttrString(pModule, "pause");
    /* pFunc is a new reference */

    if (pFunc && PyCallable_Check(pFunc)) {
        pArgs = PyTuple_New(0);
//        for (int i = 0; i < nParametros; ++i) {
//            pValue = PyInt_FromLong(args[i]);
//            if (!pValue) {
//                Py_DECREF(pArgs);
//                fprintf(stderr, "Cannot convert argument\n");
//                return 1;
//            }
//            /* pValue reference stolen here: */
//            PyTuple_SetItem(pArgs, i, pValue);
//        }
        pValue = PyObject_CallObject(pFunc, pArgs);
        Py_DECREF(pArgs);
        if (pValue != NULL) {
            //printf("Result of call: %ld\n", PyInt_AsLong(pValue));
            Py_DECREF(pValue);
        }
        else {
            Py_DECREF(pFunc);
            PyErr_Print();
            fprintf(stderr,"Call failed\n");
            return 1;
        }
    }
    else {
        if (PyErr_Occurred())
            PyErr_Print();
        fprintf(stderr, "Cannot find function run \n");
    }
    Py_XDECREF(pFunc);
    return 0;
}

int PythonAPI::callFunctionUpdateBorders()
{
    PyObject *pFunc;//*pDict,
    PyObject *pArgs, *pValue;
    //int nParametros = 15;
    pFunc = PyObject_GetAttrString(pModule, "updateBorders");
    /* pFunc is a new reference */

    Configuracao& conf = Configuracao::getInstance();
    double direita, esquerda, cima, baixo;

    direita = Utils::pxToCm(max(conf.getPositionUpperRight()[0], conf.getPositionLowerRight()[0]));
    esquerda = Utils::pxToCm(min(conf.getPositionUpperLeft()[0], conf.getPositionLowerLeft()[0]));
    cima = Utils::pxToCm(min(conf.getPositionUpperRight()[1], conf.getPositionUpperLeft()[1]));
    baixo = Utils::pxToCm(max(conf.getPositionLowerRight()[1], conf.getPositionLowerLeft()[1]));

    //cout << direita << " " << esquerda << " " << cima << " " << baixo << endl;

    if (pFunc && PyCallable_Check(pFunc)) {
        pArgs = PyTuple_New(4);
        PyTuple_SetItem(pArgs, 0, PyFloat_FromDouble(direita));
        PyTuple_SetItem(pArgs, 1, PyFloat_FromDouble(esquerda));
        PyTuple_SetItem(pArgs, 2, PyFloat_FromDouble(cima));
        PyTuple_SetItem(pArgs, 3, PyFloat_FromDouble(baixo));
        pValue = PyObject_CallObject(pFunc, pArgs);
        Py_DECREF(pArgs);
        if (pValue != NULL) {
            //printf("Result of call: %ld\n", PyInt_AsLong(pValue));
            Py_DECREF(pValue);
        }
        else {
            Py_DECREF(pFunc);
            PyErr_Print();
            fprintf(stderr,"Call failed\n");
            return 1;
        }
    }
    else {
        if (PyErr_Occurred())
            PyErr_Print();
        fprintf(stderr, "Cannot find function run \n");
    }
    Py_XDECREF(pFunc);
    return 0;
}
