import scipy.stats
from prettytable import PrettyTable


def p_value(f, dfn, dfd):
    return 1 - scipy.stats.f.cdf(f, dfn, dfd)


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
