import math

import pytest

from ..rcbd import RandomizedCompleteBlockDesign, RandomizedCompleteBlockDesign_MissingValues


class TestRCBD:
    def test_rcbd_1(self):
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

    def test_rcbd_2(self):
        exp = RandomizedCompleteBlockDesign(
            [
                [9.3, 9.4, 9.6, 10.0],
                [9.4, 9.3, 9.8, 9.9],
                [9.2, 9.4, 9.5, 9.7],
                [9.7, 9.6, 10.0, 10.2],
            ]
        )

        abs_tol = 10 ** -3
        assert math.isclose(exp.f_treatments, 14.4375, abs_tol=abs_tol)
        assert math.isclose(exp.p_treatments, 0.0009, abs_tol=abs_tol)


class TestRCBDMissing:
    def test_rcbd_missing_1(self):
        exp = RandomizedCompleteBlockDesign_MissingValues(
            [
                [18.5, 11.7, 15.4, 16.5],
                [15.7, float("nan"), 16.6, 18.6],
                [16.2, 12.9, 15.5, 12.7],
                [14.1, 14.4, 20.3, 15.7],
                [13.0, 16.9, 18.4, 16.5],
                [13.6, 12.5, 41.5, 18.0],
            ]
        )
        abs_tol = 10 ** -3
        assert math.isclose(exp.f_treatments, 0.7561, abs_tol=abs_tol)
        assert math.isclose(exp.f_blocks, 2.0859, abs_tol=abs_tol)

    def test_rcbd_missing_2(self):
        exp = RandomizedCompleteBlockDesign_MissingValues(
            [[12, 14, 12], [10, float("nan"), 8], [float("nan"), 15, 10]]
        )

        assert math.isclose(exp.f_treatments, 4.7500, abs_tol=10 ** -3)
        assert math.isclose(exp.f_blocks, 7.7500, abs_tol=10 ** -3)

    def test_rcbd_missing_3(self):
        exp = RandomizedCompleteBlockDesign_MissingValues(
            [
                [90.3, 89.2, 98.2, 93.9, 87.4, 97.9],
                [92.5, 89.5, 90.6, float("nan"), 87, 95.8],
                [85.5, 90.8, 89.6, 86.2, 88, 93.4],
                [82.5, 89.5, 85.6, 87.4, 78.9, 90.7],
            ]
        )

        abs_tol = 10 ** -3
        assert math.isclose(exp.f_treatments, 7.6241, abs_tol=abs_tol)
        assert math.isclose(exp.f_blocks, 5.2181, abs_tol=abs_tol)

    def test_rcbd_missing_throw_error(self):
        with pytest.raises(Exception):
            # 3 missing, throw exception
            RandomizedCompleteBlockDesign_MissingValues(
                [
                    [18.5, 11.7, 15.4, 16.5],
                    [15.7, float("nan"), 16.6, 18.6],
                    [16.2, 12.9, 15.5, 12.7],
                    [14.1, 14.4, float("nan"), 15.7],
                    [13.0, 16.9, 18.4, 16.5],
                    [13.6, float("nan"), 41.5, 18.0],
                ]
            )

    def test_rcbd_multiple_comparisons(self):
        exp = RandomizedCompleteBlockDesign(
            [
                [9.3, 9.4, 9.6, 10.0],
                [9.4, 9.3, 9.8, 9.9],
                [9.2, 9.4, 9.5, 9.7],
                [9.7, 9.6, 10.0, 10.2],
            ]
        )

        exp.multiple_comparisons()
