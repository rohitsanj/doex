import numpy as np
import scipy.stats
from tabulate import tabulate

__all__ = ["F_1_way_anova"]


class F_1_way_anova:
    def __init__(self, *entries):
        self.entries = entries
        self.ss_treatment = None
        self.ss_error = None
        self.ss_total = None
        self.dof_treatment = None
        self.dof_total = None
        self.dof_error = None
        self.mss_treatment = None
        self.f = None
        self.p = None

    def run(self):
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
        table = [
            ["Between treatment groups", self.dof_treatment,
                self.ss_treatment, self.mss_treatment, self.f, self.p],
            ["Within groups (error)", self.dof_error, self.ss_error, self.mss_error, "", ""],
            ["Total", self.dof_total, self.ss_total, "", "", ""]
        ]
        print(tabulate(table, headers=["Source of Variation", "DOF", "Sum of Squares",
                                       "Mean Sum of Squares", "F statistic", "p-value"]))
