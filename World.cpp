#include "World.h"

using namespace std;

World::World()
{

}

World::~World()
{

}

void World::setTeammates(Player players[]) {
    for(int i=0; i<3; i++) {
        teammates[i] = players[i];
    }
}

void World::setOpponents(Player players[3]) {
    for(int i=0; i<3; i++) {
        opponents[i] = players[i];
    }
}

void World::setPlayers(Player teammates[3], Player opponents[3]) {
    setTeammates(teammates);
    setOpponents(opponents);
}

void World::setBall(Ball &ball) {
    this->ball = ball;
}

Player World::getTeammate(unsigned int n) {
    return teammates[n];
}

Player World::getOpponents(unsigned int n) {
    return opponents[n];
}

Ball World::getBall() {
    return ball;
}

void World::toPx() {
    for(int i=0; i<3; i++) {
        Player p = teammates[i];
        teammates[i] = Player(Utils::cmToPx(p.getX()), Utils::cmToPx(p.getY()), p.getAngle());

        Player op = opponents[i];
        opponents[i] = Player(Utils::cmToPx(op.getX()), Utils::cmToPx(op.getY()), op.getAngle());
    }

    ball = Ball(Utils::cmToPx(ball.getX()), Utils::cmToPx(ball.getY()));
}

void World::toCm() {
    for(int i=0; i<3; i++) {
        Player p = teammates[i];
        teammates[i] = Player(Utils::pxToCm(p.getX()), Utils::pxToCm(p.getY()), p.getAngle());

        Player op = opponents[i];
        opponents[i] = Player(Utils::pxToCm(op.getX()), Utils::pxToCm(op.getY()), op.getAngle());
    }

    ball = Ball(Utils::pxToCm(ball.getX()), Utils::pxToCm(ball.getY()));
}

void World::print(){
    for(int i=0; i<3; i++) {
        Player p = teammates[i];
        Player o = opponents[i];
        cout << o.getX() << ", " << o.getY() << ", " << o.getAngle() << endl;
    }
}

