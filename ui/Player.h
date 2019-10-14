#ifndef PLAYER_H
#define PLAYER_H

#include <math.h>


#define TEAMMATES   0
#define OPPONENTS   1

class Player
{
    float x, y, angle;

    void setFromBlobs(float xa, float ya, float xb, float yb);

public:
    Player();
    Player(float x, float y, float angle);
    Player(float xa, float ya, float xb, float yb);
    ~Player();

    float getX();
    float getY();
    float getAngle();
};

#endif // PLAYER_H
