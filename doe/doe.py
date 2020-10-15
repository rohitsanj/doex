import numpy as np
import scipy.stats
from tabulate import tabulate

__all__ = ["f_1_way_anova"]


def f_1_way_anova(*args):
    total_sum = 0
    num_total = 0
    all_entries = np.array([])
    for a in args:
        num_total = num_total + len(a)
        total_sum = total_sum + np.sum(a)

        all_entries = np.concatenate((all_entries, a))

    y_total_average = total_sum / num_total

    assert total_sum == np.sum(all_entries)

    ss_treatment = 0
    for a in args:
        ss_treatment += len(a) * np.square(np.average(a) - y_total_average)

    ss_total = np.sum(np.square(all_entries - y_total_average))

    ss_error = ss_total - ss_treatment

    dof_treatment = len(args) - 1
    dof_total = len(all_entries) - 1
    dof_error = dof_total - dof_treatment

    mss_treatment = ss_treatment / dof_treatment
    mss_error = ss_error / dof_error

    f_statistic = mss_treatment / mss_error

    dfn = dof_treatment
    dfd = dof_error
    p = 1 - scipy.stats.f.cdf(f_statistic, dfn, dfd)

    table = [
        ["Between treatment groups", dof_treatment,
            ss_treatment, mss_treatment, f_statistic, p],
        ["Within groups (error)", dof_error, ss_error, mss_error, "", ""],
        ["Total", dof_total, ss_total, "", "", ""]
    ]

    print(tabulate(table, headers=["Source of Variation", "DOF", "Sum of Squares",
                                   "Mean Sum of Squares", "F statistic", "p-value"]))

    return f_statistic, p
