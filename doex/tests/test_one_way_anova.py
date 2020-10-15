import math

import pytest

from ..one_way_anova import OneWayANOVA


@pytest.fixture
def exp():
    return OneWayANOVA(
        [24, 28, 37, 30],
        [37, 44, 31, 35],
        [42, 47, 52, 38],
    )


class TestOneWayANOVA:
    def test_onewayanova(self, exp):
        assert math.isclose(exp.f, 7.0356, abs_tol=10 ** -3)
        assert math.isclose(exp.p, 0.0145, abs_tol=10 ** -3)

    def test_onewayanova_display(self, exp):
        exp.display()
        assert "7.0356" in exp.table.get_string()
