import numpy as np
import scipy.stats
from statsmodels.stats.libqsturng import qsturng
from prettytable import PrettyTable
from itertools import combinations


def p_value(f, dfn, dfd):
    return 1 - scipy.stats.f.cdf(f, dfn, dfd)


def get_q_crit(k, df, alpha=0.05):
    return qsturng(1 - alpha, k, df)


def get_t_value(y1, y2, sigma, n1, n2):
    return (y2 - y1) / (sigma * np.sqrt((1 / n1) + (1 / n2)))


def create_anova_table():
    float_format = ".4"

    table = PrettyTable()
    table.float_format["Sum of Squares"] = float_format
    table.float_format["Mean Sum of Squares"] = float_format
    table.float_format["F statistic"] = float_format
    table.float_format["p value"] = float_format

    table.field_names = [
        "Source of Variation",
        "DOF",
        "Sum of Squares",
        "Mean Sum of Squares",
        "F statistic",
        "p value",
    ]
    return table


def create_multi_comparisons_table():
    float_format = " .4"

    table = PrettyTable()
    table.float_format["t statistic"] = float_format

    table.field_names = ["Treatment", "t statistic", ""]
    return table


def multiple_comparisons(treatments, treatments_data, error_dof, sigma_error, alpha=0.05):
    treatment_map = {t: d for t, d in zip(treatments, treatments_data)}
    treatment_means = {t: np.average(d) for t, d in treatment_map.items()}

    k = len(treatment_means)

    q_crit = get_q_crit(k, error_dof, alpha) / np.sqrt(2)

    comparisons_list = list(combinations(treatments, 2))

    t_values = {}
    for pair in comparisons_list:
        t = get_t_value(treatment_means[pair[0]], treatment_means[pair[1]], sigma_error, k, k)
        t_values[pair] = (t, "Significant" if abs(t) > q_crit else "Not Significant")

    table = create_multi_comparisons_table()
    sorted_t_values = {k: v for k, v in sorted(t_values.items(), key=lambda item: item[0])}
    for comp, t in sorted_t_values.items():
        table.add_row(["{} vs {}".format(*comp), *t])

    return table
