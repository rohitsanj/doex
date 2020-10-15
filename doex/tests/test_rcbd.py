import math

from ..rcbd import RandomizedCompleteBlockDesign


class TestRCBD:
    def test_rcbd(self):
        exp = RandomizedCompleteBlockDesign(
            [
                [73, 68, 74, 71, 67],
                [73, 67, 75, 72, 70],
                [75, 68, 78, 73, 68],
                [73, 71, 75, 75, 69],
            ]
        )

        abs_tol = 10 ** -3
        assert math.isclose(exp.f_treatments, 2.3761, abs_tol=abs_tol)
        assert math.isclose(exp.p_treatments, 0.1211, abs_tol=abs_tol)
