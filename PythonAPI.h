#ifndef PYTHONAPI_H
#define PYTHONAPI_H

#include <Python.h>
#include <string>
#include <iostream>
#include "World.h"

class PythonAPI
{
    PyObject *pName, *pModule;

public:
    PythonAPI(char* file);
    ~PythonAPI();
    PyObject *callFunctionRun(double* args);
    PyObject *callFunctionRun(World* world, int penalty, int paused);
    int callFunctionUpdateBorders();
    int callFunctionPause();

};

#endif // PYTHONAPI_H
