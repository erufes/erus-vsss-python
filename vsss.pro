QT       += core gui
CONFIG += c++11

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = vsss
CONFIG   += console
TEMPLATE = app


INCLUDEPATH += C:\\opencv-mingw\\install\\include
INCLUDEPATH += C:\\Python27\\include
LIBS += C:\\Python27\\libs\\libpython27.a
LIBS += C:\\opencv-mingw\\install\\x64\\mingw\\lib\\libopencv_core2410.dll.a
LIBS += C:\\opencv-mingw\\install\\x64\\mingw\\lib\\libopencv_highgui2410.dll.a
LIBS += C:\\opencv-mingw\\install\\x64\\mingw\\lib\\libopencv_imgproc2410.dll.a

LIBS += C:\\opencv-mingw\\install\\x64\\mingw\\lib\\libopencv_objdetect2410.dll.a
LIBS += C:\\opencv-mingw\\install\\x64\\mingw\\lib\\libopencv_video2410.dll.a

SOURCES += main.cpp \
    VideoProcessor.cpp \
    World.cpp \
    Player.cpp \
    Ball.cpp \
    BlobProcessor.cpp \
    MainWindow.cpp \
    Settings.cpp \
    Color.cpp \
    SoccerField.cpp \
    tinyxml2.cpp \
    XMLSettingsEditor.cpp \
    CaptureThread.cpp \
    ProcessingThread.cpp \
    ColorManagement.cpp \
    ColorManagementThread.cpp \
    PythonAPI.cpp \
    PythonThread.cpp \
#    MeanShiftProcessor.cpp
#    calibracao.cpp
    Utils.cpp \
    CalibracaoArena.cpp \
    CalibracaoArenaThread.cpp

HEADERS += \
    VideoProcessor.h \
    World.h \
    Player.h \
    Ball.h \
    BlobProcessor.h \
    MainWindow.h \
    Settings.h \
    Color.h \
    SoccerField.h \
    tinyxml2.h \
    XMLSettingsEditor.h \
    Buffer.h \
    CaptureThread.h \
    ProcessingThread.h \
    ColorManagement.h \
    ColorManagementThread.h \
    PythonAPI.h \
    PythonThread.h \
    constants.h \
#    MeanShiftProcessor.h
#    calibracao.h
    Utils.h \
    Configuracao.h \
    Configuracao.h \
    CalibracaoArena.h \
    CalibracaoArenaThread.h

FORMS += MainWindow.ui \
    ColorManagement.ui \
    CalibracaoArena.ui

