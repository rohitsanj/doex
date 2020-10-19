import math

import pytest

from ..graeco_latin_square import GraecoLatinSquare


class TestLatinSquare:
    def test_latin_square(self):
        exp = GraecoLatinSquare(
            latin=[
                ["A", "B", "C", "D", "E"],
                ["B", "C", "D", "E", "A"],
                ["C", "D", "E", "A", "B"],
                ["D", "E", "A", "B", "C"],
                ["E", "A", "B", "C", "D"],
            ],
            greek=[
                ["a", "g", "e", "b", "d"],
                ["b", "d", "a", "g", "e"],
                ["g", "e", "b", "d", "a"],
                ["d", "a", "g", "e", "b"],
                ["e", "b", "d", "a", "g"],
            ],
            treatments_values=[
                [-1, -5, -6, -1, -1],
                [-8, -1, 5, 2, 11],
                [-7, 13, 1, 2, -4],
                [1, 6, 1, -2, -3],
                [-3, 5, -5, 4, 6],
            ],
        )

        abs_tol = 10 ** -3
        assert math.isclose(exp.f_greek_treatments, 1.8788, abs_tol=abs_tol)
        assert math.isclose(exp.f_latin_treatments, 10, abs_tol=abs_tol)

    def test_latin_square_raises_error_treatments(self):
        with pytest.raises(ValueError):
            GraecoLatinSquare(
                latin=[
                    ["A", "B", "D", "C", "E"],
                    ["C", "E", "A", "D", "B"],
                    ["B", "A", "C", "E", "D"],
                    ["D", "C", "E", "B", "A"],
                    ["E", "G", "B", "F", "C"],
                ],
                greek=[
                    ["a", "g", "e", "b", "d"],
                    ["b", "d", "a", "g", "e"],
                    ["g", "e", "b", "d", "a"],
                    ["d", "a", "g", "e", "b"],
                    ["e", "b", "d", "a", "g"],
                ],
                treatments_values=[
                    [8, 7, 1, 7, 3],
                    [11, 2, 7, 3, 8],
                    [4, 9, 10, 1, 5],
                    [6, 8, 6, 6, 10],
                    [4, 2, 3, 8, 8],
                ],
            )

    def test_latin_square_raises_error_invalid_sizes(self):
        with pytest.raises(ValueError):
            GraecoLatinSquare(
                latin=[
                    ["A", "B", "D", "C", "E"],
                    ["C", "E", "A", "D", "B"],
                    ["B", "A", "C", "E", "D"],
                    ["D", "C", "E", "B", "A"],
                    ["E", "G", "B", "F", "C"],
                ],
                greek=[
                    ["a", "g", "e", "b", "d"],
                    ["b", "d", "a", "g", "e"],
                    ["g", "e", "b", "d", "a"],
                    ["d", "a", "g", "e", "b"],
                    ["e", "b", "d", "a", "g"],
                    ["e", "b", "d", "a", "g"],
                ],
                treatments_values=[
                    [8, 7, 1, 7, 3],
                    [11, 2, 7, 3, 8],
                    [4, 9, 10, 1, 5],
                    [6, 8, 6, 6, 10],
                    [4, 2, 3, 8, 8],
                ],
            )
