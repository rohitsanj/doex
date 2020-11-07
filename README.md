[![Build Status](https://github.com/rohitsanj/doex/workflows/CI/badge.svg)](https://github.com/rohitsanj/doex/actions)
[![Downloads](https://pepy.tech/badge/doex)](https://pepy.tech/project/doex)
[![Downloads](https://pepy.tech/badge/doex/week)](https://pepy.tech/project/doex)
[![image](https://codecov.io/github/rohitsanj/doex/coverage.svg?branch=master)](https://codecov.io/github/rohitsanj/doex?branch=master)
[![Documentation Status](https://readthedocs.org/projects/doex/badge/?version=latest)](https://doex.rohitsanjay.com/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/doex.svg)](https://pypi.org/project/doex/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rohitsanj/doex/master?filepath=notebooks%2Fdoex-demo.ipynb)

# doex - Design and Analysis of Experiments

Python library for conducting design of experiments.

## Installation

```bash
pip install doex
```

## Online Demo

Try out `doex` in an online Jupyter Notebook - [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/rohitsanj/doex/master?filepath=notebooks%2Fdoex-demo.ipynb)

## Sample usage

```python
import doex

exp = doex.OneWayANOVA(
    [24, 28, 37, 30], # Treatment 1
    [37, 44, 31, 35], # Treatment 2
    [42, 47, 52, 38], # Treatment 3
)
```

```
+---------------------+-----+----------------+---------------------+-------------+---------+
| Source of Variation | DOF | Sum of Squares | Mean Sum of Squares | F statistic | p value |
+---------------------+-----+----------------+---------------------+-------------+---------+
|      Treatments     |  2  |    450.6667    |       225.3333      |    7.0356   |  0.0145 |
|        Error        |  9  |    288.2500    |       32.0278       |             |         |
|        Total        |  11 |    738.9167    |                     |             |         |
+---------------------+-----+----------------+---------------------+-------------+---------+
```

## Documentation

Visit the doex [documentation][documentation].

## Implementations

- [Completely Randomized Design / One-Way ANOVA](https://doex.rohitsanjay.com/en/latest/examples.html#completely-randomized-design)
- [Randomized Complete Block Design / Two-Way ANOVA](https://doex.rohitsanjay.com/en/latest/examples.html#randomized-complete-block-design)
- [Latin Square Design](https://doex.rohitsanjay.com/en/latest/examples.html#latin-square-design)
- [Graeco-Latin Square Design](https://doex.rohitsanjay.com/en/latest/examples.html#graeco-latin-square-design)
- [Randomized Complete Block Design with missing values](https://doex.rohitsanjay.com/en/latest/examples.html#randomized-complete-block-design-with-missing-values)
- Balanced Incomplete Block Design (TODO)
- Factorial Designs (TODO)

## Acknowledgements

- Adapted from [https://github.com/pawanaichra/doe](https://github.com/pawanaichra/doe).

[documentation]: https://doex.rohitsanjay.com/
