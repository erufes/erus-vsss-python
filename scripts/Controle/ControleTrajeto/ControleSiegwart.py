from .IControleTrajeto import IcontroleTrajeto
from ...Geometria import Ponto, to180range
import math as m


class ControleSiegwart(IcontroleTrajeto):

    __kRho = 1.85
    __kAlpha = 9.7
    __kBeta = -0.01
    __PI = 3.14159

    def controle(self, actualValue, objective, speed):
        xa, ya, ta = actualValue
        xo, yo, to = objective

        ta = to180range(ta * ControleSiegwart.__PI / 180)
        rho = Ponto(xa, ya).distancia(Ponto(xo, yo))
        lamb = m.atan2(yo - ya, xo - xa)

        if rho < 3:
            lamb = 0

        alpha = to180range(lamb - ta)
        beta = to - lamb

        linearSpeed = - ControleSiegwart.__kRho * rho
        angularSpeed = ControleSiegwart.__kAlpha * alpha + ControleSiegwart.__kBeta * beta

        scale = speed / linearSpeed
        linearSpeed *= scale
        angularSpeed *= scale

        if rho < 3:
            linearSpeed = 0
            angularSpeed *= 0.4

        if m.fabs(alpha) > 0.5 * ControleSiegwart.__PI:
            linearSpeed = - linearSpeed

        result = ((linearSpeed - angularSpeed * 3.35) / 2,
                  (linearSpeed + angularSpeed * 3.35) / 2)
        maxSpeed = max(m.fabs(result[0]), m.fabs(result[1]))

        if maxSpeed > 100:
            result = (result[0] * 100 / m.fabs(maxSpeed),
                      result[1] * 100 / m.fabs(maxSpeed))

        return result
