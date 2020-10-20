import math

import pytest

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

    def test_latin_square_raises_error_shape_mismatch(self):
        with pytest.raises(ValueError):
            LatinSquare(
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
                    [4, 2, 3, 8, 8],  # Extra row
                ],
            )

    def test_latin_square_raises_error_treatments(self):
        with pytest.raises(ValueError):
            LatinSquare(
                [
                    ["A", "B", "D", "C", "E"],
                    ["C", "E", "A", "D", "B"],
                    ["B", "A", "C", "E", "D"],
                    ["D", "C", "E", "B", "A"],
                    ["E", "G", "B", "F", "C"],
                ],
                [
                    [8, 7, 1, 7, 3],
                    [11, 2, 7, 3, 8],
                    [4, 9, 10, 1, 5],
                    [6, 8, 6, 6, 10],
                    [4, 2, 3, 8, 8],
                ],
            )

    def test_latin_square_missing_1(self):
        exp = LatinSquare(
            [
                ["A", "C", "B", "D"],
                ["C", "B", "D", "A"],
                ["B", "D", "A", "C"],
                ["D", "A", "C", "B"],
            ],
            [[12, 19, 10, 8], [18, 12, 6, float("nan")], [22, 10, 5, 21], [12, 7, 27, 17]],
        )

        abs_tol = 10 ** -3
        assert math.isclose(exp.f_treatments, 15.0143, abs_tol=abs_tol)
        assert math.isclose(exp.f_rows, 2.5857, abs_tol=abs_tol)
        assert math.isclose(exp.f_columns, 1.3714, abs_tol=abs_tol)

    def test_latin_square_multiple_comparisons(self):
        exp = LatinSquare(
            [
                ["C", "D", "B", "A"],
                ["A", "B", "D", "C"],
                ["D", "C", "A", "B"],
                ["B", "A", "C", "D"],
            ],
            [
                [235, 236, 218, 268],
                [251, 241, 227, 229],
                [234, 273, 274, 226],
                [195, 270, 230, 225],
            ],
        )

        exp.multiple_comparisons()
