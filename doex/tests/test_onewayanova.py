import pytest
import numpy.testing as npt
from ..onewayanova import OneWayANOVA


@pytest.fixture
def exp():
    return OneWayANOVA(
        [24, 28, 37, 30],
        [37, 44, 31, 35],
        [42, 47, 52, 38],
    )


class TestOneWayANOVA:
    def test_onewayanova(self, exp):
        npt.assert_almost_equal(exp.f, 7.0356, decimal=3)
        npt.assert_almost_equal(exp.p, 0.0145, decimal=3)

    def test_onewayanova_display(self, exp):
        exp.display()
        assert "7.0356" in exp.table.get_string()
