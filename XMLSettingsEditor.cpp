#include "XMLSettingsEditor.h"

XMLSettingsEditor::XMLSettingsEditor() {

}

XMLSettingsEditor::XMLSettingsEditor(const char* fileName) {
    loadFile(fileName);
}

XMLSettingsEditor::~XMLSettingsEditor() {

}

bool XMLSettingsEditor::loadFile(const char *fileName) {
    doc.LoadFile(fileName);
    if(doc.ErrorID() != 0) {
        cerr << "ERROR: cannot open " << fileName << endl;
        return false;
    }

    config = doc.FirstChildElement("config");
    if(config == NULL) {
        cerr << "ERROR: node \"config\" does not exist" << endl;
        return false;
    }

    colorList = config->FirstChildElement("colors");
    if(colorList != NULL) {
        readColorList(colorList);
    }

    readSettings();

    return true;
}

void XMLSettingsEditor::readColorList(XMLElement *colorListElement) {
    XMLElement *colorElement = colorListElement->FirstChildElement("color");
    while(colorElement != NULL) {
        const char *colorName = colorElement->Attribute("name");

        if(strcmp(colorName, "blue") == 0) {
            colors[COLOR_BLUE] = colorElement;
        } else if(strcmp(colorName, "yellow") == 0) {
            colors[COLOR_YELLOW] = colorElement;
        } else if(strcmp(colorName, "orange") == 0) {
            colors[COLOR_ORANGE] = colorElement;
        } else if(strcmp(colorName, "color1") == 0) {
            colors[COLOR_1] = colorElement;
        } else if(strcmp(colorName, "color2") == 0) {
            colors[COLOR_2] = colorElement;
        } else if(strcmp(colorName, "color3") == 0) {
            colors[COLOR_3] = colorElement;
        }

        colorElement = colorElement->NextSiblingElement("color");
    }
}

void XMLSettingsEditor::readSettings() {

}

