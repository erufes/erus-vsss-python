#ifndef XMLSETTINGSEDITOR_H
#define XMLSETTINGSEDITOR_H

#include <cstring>
#include <iostream>

#include "tinyxml2.h"
#include "Settings.h"

using namespace tinyxml2;

class XMLSettingsEditor
{
    Settings settings;
    XMLDocument doc;
    XMLElement *config, *colorList, *colors[6];

    void readColorList(XMLElement *colorListElement);
    void readSettings();

public:
    XMLSettingsEditor();
    XMLSettingsEditor(const char *fileName);
    ~XMLSettingsEditor();

    bool loadFile(const char *fileName);
    void saveFile(const char *fileName);
    void saveFile();

    Settings getSettings() const;
    void setSettings(const Settings &value);
};

#endif // XMLSETTINGSEDITOR_H
