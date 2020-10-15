import math

from ..one_way_anova import OneWayANOVA


class TestOneWayANOVA:
    def test_onewayanova(self):
        exp = OneWayANOVA(
            [24, 28, 37, 30],
            [37, 44, 31, 35],
            [42, 47, 52, 38],
        )

        abs_tol = 10 ** -3
        assert math.isclose(exp.f, 7.0356, abs_tol)
        assert math.isclose(exp.p, 0.0145, abs_tol)
