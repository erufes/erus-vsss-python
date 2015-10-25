#ifndef WORLD_H
#define WORLD_H

#include "Player.h"
#include "Ball.h"
#include "Utils.h"
#include <iostream>

class World
{
    Player teammates[3], opponents[3];
    Ball ball;

public:
    World();
    ~World();

    void setPlayer(unsigned int n, unsigned int team, Player &player);
    void setTeammate(unsigned int n, Player &player);
    void setOpponent(unsigned int n, Player &player);
    void setTeammates(Player players[]);
    void setOpponents(Player players[3]);
    void setPlayers(Player teammates[3], Player opponents[3]);
    void setBall(Ball &ball);

    Player getTeammate(unsigned int n);
    Ball getBall();

    void toPx();
    void toCm();

    void print();
};

#endif // WORLD_H
