import numpy as np

from .utils import p_value, create_anova_table


class CompletelyRandomizedDesign:
    def __init__(self, *entries):
        self.entries = entries

        all_entries = np.array([])
        for entry in self.entries:
            all_entries = np.concatenate((all_entries, entry))

        y_total_average = np.average(all_entries)

        # Calculate Sum of Squares
        self.ss_treatment = np.sum(
            [len(entry) * np.square(np.average(entry) - y_total_average) for entry in self.entries]
        )
        self.ss_total = np.sum(np.square(all_entries - y_total_average))
        self.ss_error = self.ss_total - self.ss_treatment

        # Calculate Degrees of Freedom
        self.dof_treatment = len(self.entries) - 1
        self.dof_total = len(all_entries) - 1
        self.dof_error = self.dof_total - self.dof_treatment

        self.mss_treatment = self.ss_treatment / self.dof_treatment
        self.mss_error = self.ss_error / self.dof_error

        self.f = self.mss_treatment / self.mss_error
        self.p = p_value(self.f, self.dof_treatment, self.dof_error)

        # Display table
        self.table = self._create_table()
        print(self.table)

    def _create_table(self):
        table = create_anova_table()

        rows = [
            [
                "Treatments",
                self.dof_treatment,
                self.ss_treatment,
                self.mss_treatment,
                self.f,
                self.p,
            ],
            ["Error", self.dof_error, self.ss_error, self.mss_error, "", ""],
            ["Total", self.dof_total, self.ss_total, "", "", ""],
        ]

        for row in rows:
            table.add_row(row)

        return table


# Single factor CRD is equivalent to One-Way ANOVA
OneWayANOVA = CompletelyRandomizedDesign
