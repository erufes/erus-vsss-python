#ifndef BALL_H
#define BALL_H

// criacao da classe de bola na qual vai ter dois atribudos
// que sao as coordenadas no campo: X e Y
class Ball
{
    float x, y;

public:
    Ball();
    Ball(float x, float y);
    ~Ball();

    float getX();
    float getY();
};

#endif // BALL_H
