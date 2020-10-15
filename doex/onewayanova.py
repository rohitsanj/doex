import numpy as np
import scipy.stats
from prettytable import PrettyTable


class OneWayANOVA:
    def __init__(self, *entries):
        self.entries = entries
        self.float_format = ".4"

        all_entries = np.array([])
        for entry in self.entries:
            all_entries = np.concatenate((all_entries, entry))

        y_total_average = np.average(all_entries)

        # Calculate Sum of Squares
        self.ss_treatment = np.sum([
            len(entry) * np.square(np.average(entry) - y_total_average)
            for entry in self.entries
        ])
        self.ss_total = np.sum(np.square(all_entries - y_total_average))
        self.ss_error = self.ss_total - self.ss_treatment

        # Calculate Degrees of Freedom
        self.dof_treatment = len(self.entries) - 1
        self.dof_total = len(all_entries) - 1
        self.dof_error = self.dof_total - self.dof_treatment

        self.mss_treatment = self.ss_treatment / self.dof_treatment
        self.mss_error = self.ss_error / self.dof_error

        self.f = self.mss_treatment / self.mss_error
        self.p = 1 - scipy.stats.f.cdf(self.f, self.dof_treatment, self.dof_error)

    def display(self):
        table = PrettyTable()
        table.float_format["Sum of Squares"] = self.float_format
        table.float_format["Mean Sum of Squares"] = self.float_format
        table.float_format["F statistic"] = self.float_format
        table.float_format["p value"] = self.float_format

        table.field_names = [
            "Source of Variation",
            "DOF",
            "Sum of Squares",
            "Mean Sum of Squares",
            "F statistic",
            "p value"
        ]

        rows = [
            ["Between treatment groups", self.dof_treatment,
                self.ss_treatment, self.mss_treatment, self.f, self.p],
            ["Within groups (error)", self.dof_error, self.ss_error, self.mss_error, "", ""],
            ["Total", self.dof_total, self.ss_total, "", "", ""]
        ]

        for row in rows:
            table.add_row(row)

        print(table)
