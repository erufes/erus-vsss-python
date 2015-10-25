#ifndef BALL_H
#define BALL_H


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
