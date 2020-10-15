# doex - Design of Experiments

Python library for conducting design of experiments

## Sample usage

```python
import doex

exp = doex.OneWayANOVA(
    [24, 28, 37, 30], # Treatment 1
    [37, 44, 31, 35], # Treatment 2
    [42, 47, 52, 38], # Treatment 3
)
exp.display()
```

Output of above snippet:

```
+--------------------------+-----+----------------+---------------------+-------------+---------+
|   Source of Variation    | DOF | Sum of Squares | Mean Sum of Squares | F statistic | p value |
+--------------------------+-----+----------------+---------------------+-------------+---------+
| Between treatment groups |  2  |    450.6667    |       225.3333      |    7.0356   |  0.0145 |
|  Within groups (error)   |  9  |    288.2500    |       32.0278       |             |         |
|          Total           |  11 |    738.9167    |                     |             |         |
+--------------------------+-----+----------------+---------------------+-------------+---------+
```

## Installation

```bash
pip install doex
```

## Documentation

Visit the doex [documentation][documentation].

## Implementations

- [x] One-way ANOVA
- [ ] Two-way ANOVA
- [ ] Completely Randomized Design
- [ ] Randomized Complete Block Design
- [ ] Randomized Complete Block Design with missing values
- [ ] Latin Square Design
- [ ] Graeco-Latin Square Design
- [ ] Balanced Incomplete Block Design
- [ ] Factorial Designs

## References

- Adapted from [https://github.com/pawanaichra/doex](https://github.com/pawanaichra/doex).

[documentation]: https://doex.readthedocs.io/
