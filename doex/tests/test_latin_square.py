import math

from ..latin_square import LatinSquare


class TestLatinSquare:
    def test_latin_square(self):
        exp = LatinSquare(
            [
                ["A", "B", "D", "C", "E"],
                ["C", "E", "A", "D", "B"],
                ["B", "A", "C", "E", "D"],
                ["D", "C", "E", "B", "A"],
                ["E", "D", "B", "A", "C"],
            ],
            [
                [8, 7, 1, 7, 3],
                [11, 2, 7, 3, 8],
                [4, 9, 10, 1, 5],
                [6, 8, 6, 6, 10],
                [4, 2, 3, 8, 8],
            ],
        )
        abs_tol = 10 ** -3
        assert math.isclose(exp.f_treatments, 11.3092, abs_tol=abs_tol)
        assert math.isclose(exp.f_rows, 1.2345, abs_tol=abs_tol)
        assert math.isclose(exp.f_columns, 0.9787, abs_tol=abs_tol)

        assert math.isclose(exp.p_treatments, 0.0005, abs_tol=abs_tol)
        assert math.isclose(exp.p_rows, 0.3476, abs_tol=abs_tol)
        assert math.isclose(exp.p_columns, 0.4550, abs_tol=abs_tol)
