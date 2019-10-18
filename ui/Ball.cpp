#include "Ball.h"

Ball::Ball() {

}

Ball::Ball(float x, float y)
{
    this->x = x;
    this->y = y;
}

Ball::~Ball()
{

}

float Ball::getX() {
    return x;
}

float Ball::getY() {
    return y;
}

