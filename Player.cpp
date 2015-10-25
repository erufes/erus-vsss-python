#include "Player.h"
#include <iostream>
using namespace std;

Player::Player() {

}

Player::Player(float x, float y, float angle) {
    this->x = x;
    this->y = y;
    this->angle = angle;
}

Player::~Player() {

}

Player::Player(float xa, float ya, float xb, float yb) {
    setFromBlobs(xa, ya, xb, yb);
}

void Player::setFromBlobs(float xa, float ya, float xb, float yb) {
    x = 0.5 * (xa + xb);
    y = 0.5 * (ya + yb);
    angle = atan2(yb - ya, xb - xa);
}

float Player::getX() {
    return x;
}

float Player::getY() {
    return y;
}

float Player::getAngle() {
    return angle;
}

