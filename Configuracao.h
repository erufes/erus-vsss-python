#ifndef CONFIGURACAO_H
#define CONFIGURACAO_H

#include <opencv2/core/core.hpp>
#include "tinyxml2.h"
#include <iostream>


class Configuracao {
public:
    static Configuracao& getInstance() {
        static Configuracao instance; // Guaranteed to be destroyed.
        // Instantiated on first use.
        return instance;
    }
    int arena_left_upper[2];
    int arena_left_lower[2];
    int arena_right_upper[2];
    int arena_right_lower[2];
    bool quadrado[];

private:
    Configuracao() {
        arena_left_upper[0] = 1;
        arena_left_upper[1] = 1;
        arena_left_lower[0] = 1;
        arena_left_lower[1] = 1;
        arena_right_upper[0] = 1;
        arena_right_upper[1] = 1;
        arena_right_lower[0] = 1;
        arena_right_lower[1] = 1;
        *quadrado = false;

        blueLowerBound = NULL;
        blueUpperBound = NULL;
        yellowLowerBound = NULL;
        yellowUpperBound = NULL;
        orangeLowerBound = NULL;
        orangeUpperBound = NULL;
        color1LowerBound = NULL;
        color1UpperBound = NULL;
        color2LowerBound = NULL;
        color2UpperBound = NULL;
        color3LowerBound = NULL;
        color3UpperBound = NULL;
    }                   // Constructor? (the {} brackets) are needed here.

    // C++ 11
    // =======
    // We can use the better technique of deleting the methods
    // we don't want.
    Configuracao(Configuracao const&) = delete;
    void operator=(Configuracao const&) = delete;

    cv::Scalar *blueLowerBound;
    cv::Scalar *blueUpperBound;
    cv::Scalar *yellowLowerBound;
    cv::Scalar *yellowUpperBound;
    cv::Scalar *orangeLowerBound;
    cv::Scalar *orangeUpperBound;
    cv::Scalar *color1LowerBound;
    cv::Scalar *color1UpperBound;
    cv::Scalar *color2LowerBound;
    cv::Scalar *color2UpperBound;
    cv::Scalar *color3LowerBound;
    cv::Scalar *color3UpperBound;

public:

    float Calcula_Distancia(float x1,float y1,float x2, float y2)
    {
        float x = x1 - x2;
        float y = y1 - y2;
        return sqrt(x * x + y * y);
    }

    double getComprimentoArena() {
        return 150.0;
    }

    void setStateCalibracao(bool state){
        *quadrado = state;
    }

    bool getStateCalibracao(){
        return *quadrado;
    }


    cv::Scalar getPositionUpperLeft() {
        if(arena_left_upper != NULL) {
            return cv::Scalar(arena_left_upper[0], arena_left_upper[1]);
        }
        return cv::Scalar();
    }

    void setPositionUpperLeft(int x, int y) {
        arena_left_upper[0] = x;
        arena_left_upper[1] = y;
    }

    cv::Scalar getPositionUpperRight() {
        if(arena_right_upper != NULL) {
            return cv::Scalar(arena_right_upper[0], arena_right_upper[1]);
        }
        return cv::Scalar();
    }

    void setPositionUpperRight(int x, int y) {
        arena_right_upper[0] = x;
        arena_right_upper[1] = y;
    }

    cv::Scalar getPositionLowerLeft() {
        if(arena_left_lower != NULL) {
            return cv::Scalar(arena_left_lower[0], arena_left_lower[1]);
        }
        return cv::Scalar();
    }

    void setPositionLowerLeft(int x, int y) {
        arena_left_lower[0] = x;
        arena_left_lower[1] = y;
    }

    cv::Scalar getPositionLowerRight() {
        if(arena_right_lower != NULL) {
            return cv::Scalar(arena_right_lower[0], arena_right_lower[1]);
        }
        return cv::Scalar();
    }

    void setPositionLowerRight(int x, int y) {
        arena_right_lower[0] = x;
        arena_right_lower[1] = y;
    }

    cv::Scalar *getBlueLowerBound() {
        return blueLowerBound;
    }

    void setBlueLowerBound(cv::Scalar value) {
        if(blueLowerBound != NULL) {
            delete blueLowerBound;
        }

        blueLowerBound = new cv::Scalar(value);
    }

    cv::Scalar *getBlueUpperBound() {
        return blueUpperBound;
    }

    void setBlueUpperBound(cv::Scalar value) {
        if(blueUpperBound != NULL) {
            delete blueUpperBound;
        }

        blueUpperBound = new cv::Scalar(value);
    }

    cv::Scalar *getYellowLowerBound() {
        return yellowLowerBound;
    }

    void setYellowLowerBound(cv::Scalar value) {
        if(yellowLowerBound != NULL) {
            delete yellowLowerBound;
        }

        yellowLowerBound = new cv::Scalar(value);
    }

    cv::Scalar *getYellowUpperBound() {
        return yellowUpperBound;
    }

    void setYellowUpperBound(cv::Scalar value) {
        if(yellowUpperBound != NULL) {
            delete yellowUpperBound;
        }

        yellowUpperBound = new cv::Scalar(value);
    }


    cv::Scalar *getOrangeLowerBound() {
        return orangeLowerBound;
    }

    void setOrangeLowerBound(cv::Scalar value) {
        if(orangeLowerBound != NULL) {
            delete orangeLowerBound;
        }

        orangeLowerBound = new cv::Scalar(value);
    }

    cv::Scalar *getOrangeUpperBound() {
        return orangeUpperBound;
    }

    void setOrangeUpperBound(cv::Scalar value) {
        if(orangeUpperBound != NULL) {
            delete orangeUpperBound;
        }

        orangeUpperBound = new cv::Scalar(value);
    }

    cv::Scalar *getColor1LowerBound() {
        return color1LowerBound;
    }

    void setColor1LowerBound(cv::Scalar value) {
        if(color1LowerBound != NULL) {
            delete color1LowerBound;
        }

        color1LowerBound = new cv::Scalar(value);
    }

    cv::Scalar *getColor1UpperBound() {
        return color1UpperBound;
    }

    void setColor1UpperBound(cv::Scalar value) {
        if(color1UpperBound != NULL) {
            delete color1UpperBound;
        }

        color1UpperBound = new cv::Scalar(value);
    }


    cv::Scalar *getColor2LowerBound() {
        return color2LowerBound;
    }

    void setColor2LowerBound(cv::Scalar value) {
        if(color2LowerBound != NULL) {
            delete color2LowerBound;
        }

        color2LowerBound = new cv::Scalar(value);
    }

    cv::Scalar *getColor2UpperBound() {
        return color2UpperBound;
    }

    void setColor2UpperBound(cv::Scalar value) {
        if(color2UpperBound != NULL) {
            delete color2UpperBound;
        }

        color2UpperBound = new cv::Scalar(value);
    }


    cv::Scalar *getColor3LowerBound() {
        return color3LowerBound;
    }

    void setColor3LowerBound(cv::Scalar value) {
        if(color3LowerBound != NULL) {
            delete color3LowerBound;
        }

        color3LowerBound = new cv::Scalar(value);
    }

    cv::Scalar *getColor3UpperBound() {
        return color3UpperBound;
    }

    void setColor3UpperBound(cv::Scalar value) {
        if(color3UpperBound != NULL) {
            delete color3UpperBound;
        }

        color3UpperBound = new cv::Scalar(value);
    }

    bool saveToFile(const char *fullPath) {
        Configuracao &conf = Configuracao::getInstance();
        tinyxml2::XMLDocument doc;

        tinyxml2::XMLElement *config = doc.NewElement("config");
        doc.LinkEndChild(config);

        tinyxml2::XMLElement *colors = doc.NewElement("colors");
        config->LinkEndChild(colors);

        if(conf.getBlueLowerBound() != NULL && conf.getBlueUpperBound() != NULL) {
            createColorElementXml(&doc, colors, "blue", conf.getBlueLowerBound(), conf.getBlueUpperBound());
        }

        if(conf.getYellowLowerBound() != NULL && conf.getYellowUpperBound() != NULL) {
            createColorElementXml(&doc, colors, "yellow", conf.getYellowLowerBound(), conf.getYellowUpperBound());
        }

        if(conf.getOrangeLowerBound() != NULL && conf.getOrangeUpperBound() != NULL) {
            createColorElementXml(&doc, colors, "orange", conf.getOrangeLowerBound(), conf.getOrangeUpperBound());
        }

        if(conf.getColor1LowerBound() != NULL && conf.getColor1UpperBound() != NULL) {
            createColorElementXml(&doc, colors, "color1", conf.getColor1LowerBound(), conf.getColor1UpperBound());
        }

        if(conf.getColor2LowerBound() != NULL && conf.getColor2UpperBound() != NULL) {
            createColorElementXml(&doc, colors, "color2", conf.getColor2LowerBound(), conf.getColor2UpperBound());
        }

        if(conf.getColor3LowerBound() != NULL && conf.getColor3UpperBound() != NULL) {
            createColorElementXml(&doc, colors, "color3", conf.getColor3LowerBound(), conf.getColor3UpperBound());
        }

        tinyxml2::XMLElement *field = doc.NewElement("field");
        config->LinkEndChild(field);

        tinyxml2::XMLElement *side0 = doc.NewElement("side");
        side0->SetAttribute("name", "0");
        field->LinkEndChild(side0);

        tinyxml2::XMLElement *corner = doc.NewElement("corner");
        corner->SetAttribute("position", "upper-left");
        corner->SetAttribute("x", std::to_string(conf.getPositionUpperLeft()[0]).c_str());
        corner->SetAttribute("y", std::to_string(conf.getPositionUpperLeft()[1]).c_str());
        side0->LinkEndChild(corner);

        corner = doc.NewElement("corner");
        corner->SetAttribute("position", "upper-right");
        corner->SetAttribute("x", std::to_string(conf.getPositionUpperRight()[0]).c_str());
        corner->SetAttribute("y", std::to_string(conf.getPositionUpperRight()[1]).c_str());
        side0->LinkEndChild(corner);

        corner = doc.NewElement("corner");
        corner->SetAttribute("position", "lower-left");
        corner->SetAttribute("x", std::to_string(conf.getPositionLowerLeft()[0]).c_str());
        corner->SetAttribute("y", std::to_string(conf.getPositionLowerLeft()[1]).c_str());
        side0->LinkEndChild(corner);

        corner = doc.NewElement("corner");
        corner->SetAttribute("position", "lower-right");
        corner->SetAttribute("x", std::to_string(conf.getPositionLowerRight()[0]).c_str());
        corner->SetAttribute("y", std::to_string(conf.getPositionLowerRight()[1]).c_str());
        side0->LinkEndChild(corner);

        doc.SaveFile(fullPath);

        return true;
    }

    void loadFile(const char *fullPath) {
        Configuracao &conf = Configuracao::getInstance();

        float lower[3];
        tinyxml2::XMLDocument doc;
        doc.LoadFile(fullPath);
        tinyxml2::XMLElement *config = doc.FirstChildElement("config");
        tinyxml2::XMLElement *colors = config->FirstChildElement("colors");
        if(colors != NULL) {
            tinyxml2::XMLElement *color = colors->FirstChildElement("color");
            int i=-1;
            while(1) {
                if(color != NULL) {
                    //std::cout << "color";
                    tinyxml2::XMLElement *lb = color->FirstChildElement("lowerbound");
                    tinyxml2::XMLElement *ub = color->FirstChildElement("upperbound");

                    //tinyxml2::XMLElement *color1 = color->FirstChildElement("blue");
                    //  std::cout << color1->FirstChildElement("lowerbound")->Attribute("h");
                    if(lb != NULL && ub != NULL) {
                        float h,s,v;

                        h = atof(ub->Attribute("h"));
                        s = atof(ub->Attribute("s"));
                        v = atof(ub->Attribute("v"));
                        cv::Scalar lower = cv::Scalar(atof(lb->Attribute("h")),atof(lb->Attribute("s")),atof(lb->Attribute("v")));
                        cv::Scalar upper = cv::Scalar(h,s,v);
                        //                    std::cout << cores_lower[i] << std::endl;
                        //                    std::cout << cores_upper[i] << std::endl;

                        std::string buffer = color->Attribute("name");
                        //                    std::cout << buffer << std::endl;
                        //                    std::cout << lower << std::endl;
                        //                    std::cout << upper << std::endl;

                        if(buffer.compare("blue") == 0) {
                            conf.setBlueLowerBound(lower);
                            conf.setBlueUpperBound(upper);
                        } else if(buffer.compare("yellow") == 0) {
                            conf.setYellowLowerBound(lower);
                            conf.setYellowUpperBound(upper);
                        } else if(buffer.compare("orange") == 0) {
                            conf.setOrangeLowerBound(lower);
                            conf.setOrangeUpperBound(upper);
                        } else if(buffer.compare("color1") == 0) {
                            conf.setColor1LowerBound(lower);
                            conf.setColor1UpperBound(upper);
                        } else if(buffer.compare("color2") == 0) {
                            conf.setColor2LowerBound(lower);
                            conf.setColor2UpperBound(upper);
                        } else if(buffer.compare("color3") == 0) {
                            conf.setColor3LowerBound(lower);
                            conf.setColor3UpperBound(upper);
                        }

                        color = color->NextSiblingElement();
                    }
                } else {
                    break;
                }
            }
        }

        tinyxml2::XMLElement *field = config->FirstChildElement("field");
        if(field != NULL) {
            std::cout << "entrou field" << std::endl;
            tinyxml2::XMLElement *side = field->FirstChildElement("side");
            if(side != NULL) {
                std::cout << "entrou side" << std::endl;
                std::string name = side->Attribute("name");
                if(name.compare("0") == 0) {
                    std::cout << "entrou side 0" << std::endl;
                    tinyxml2::XMLElement *corner = side->FirstChildElement("corner");
                    while(corner != NULL) {
                        std::string attribute = corner->Attribute("position");
                        int x = atoi(corner->Attribute("x"));
                        int y = atoi(corner->Attribute("y"));

                        if(attribute.compare("upper-left") == 0) {
                            conf.setPositionUpperLeft(x, y);
                        } else if(attribute.compare("upper-right") == 0) {
                            conf.setPositionUpperRight(x, y);
                        } else if(attribute.compare("lower-left") == 0) {
                            conf.setPositionLowerLeft(x, y);
                        } else if(attribute.compare("lower-right") == 0) {
                            conf.setPositionLowerRight(x, y);
                        }

                        corner = corner->NextSiblingElement("corner");
                    }
                }
            }
        }

        return;
    }

    int hbins = 30, sbins = 32, w_camera = 480 , h_camera = 640, robot_size = 60;
    int histSize[2] = {hbins, sbins};
    float hranges[2] = {0, 180};
    float sranges[2] = { 0, 256 };
    const float* ranges[2] = { hranges, sranges };
    int channels[2] = {0, 1};
    float comprimentoArena = 170; // cm
    cv::Point verticeComprimentoArena1 = cv::Point(95, 64);
    cv::Point verticeComprimentoArena2 = cv::Point(560, 65);

    void createColorElementXml(tinyxml2::XMLDocument *doc, tinyxml2::XMLElement *parent, char *name, cv::Scalar *lowerBound, cv::Scalar *upperBound) {
        tinyxml2::XMLElement *color = doc->NewElement("color");
        color->SetAttribute("name", name);
        parent->LinkEndChild(color);

        tinyxml2::XMLElement *lowerBoundElement = doc->NewElement("lowerbound");
        lowerBoundElement->SetAttribute("h", std::to_string(lowerBound->val[0]).c_str());
        lowerBoundElement->SetAttribute("s", std::to_string(lowerBound->val[1]).c_str());
        lowerBoundElement->SetAttribute("v", std::to_string(lowerBound->val[2]).c_str());
        color->LinkEndChild(lowerBoundElement);

        tinyxml2::XMLElement *upperBoundElement = doc->NewElement("upperbound");
        upperBoundElement->SetAttribute("h", std::to_string(upperBound->val[0]).c_str());
        upperBoundElement->SetAttribute("s", std::to_string(upperBound->val[1]).c_str());
        upperBoundElement->SetAttribute("v", std::to_string(upperBound->val[2]).c_str());
        color->LinkEndChild(upperBoundElement);
    }
};

#endif // CONFIGURACAO_H
