import numpy as np

from .utils import p_value, create_anova_table


class RandomizedCompleteBlockDesign:
    def __init__(self, data):
        self.data = np.array(data)
        print(self.data.shape)
        n_treatments, n_blocks = self.data.shape

        N = 0
        for entry in self.data:
            N += len(entry)

        self.correction_factor = np.square(np.sum(self.data)) / N

        # Calculate Sum of Squares
        self.row_totals = np.sum(self.data, axis=1)
        self.ss_treatments = np.sum(np.square(self.row_totals)) / n_blocks
        self.ss_treatments = self.ss_treatments - self.correction_factor

        self.column_totals = np.sum(self.data, axis=0)
        self.ss_blocks = np.sum(np.square(self.column_totals)) / n_treatments
        self.ss_blocks = self.ss_blocks - self.correction_factor

        self.ss_total = np.sum(np.square(self.data)) - self.correction_factor

        self.ss_error = self.ss_total - (self.ss_treatments + self.ss_blocks)

        # Calculate Degrees of Freedom
        self.dof_treatments = n_treatments - 1
        self.dof_blocks = n_blocks - 1
        self.dof_total = N - 1
        self.dof_error = self.dof_total - (self.dof_treatments + self.dof_blocks)

        # Calculate Mean Sum of Squares
        self.mss_treatments = self.ss_treatments / self.dof_treatments
        self.mss_blocks = self.ss_blocks / self.dof_blocks
        self.mss_error = self.ss_error / self.dof_error

        self.f_treatments = self.mss_treatments / self.mss_error
        self.f_blocks = self.mss_blocks / self.mss_error

        self.p_treatments = p_value(self.f_treatments, self.dof_treatments, self.dof_error)
        self.p_blocks = p_value(self.f_blocks, self.dof_blocks, self.dof_error)

        # Display results
        self.table = self._create_table()
        print(self.table)

    def _create_table(self):
        table = create_anova_table()

        rows = [
            [
                "Treatments",
                self.dof_treatments,
                self.ss_treatments,
                self.mss_treatments,
                self.f_treatments,
                self.p_treatments,
            ],
            [
                "Blocks",
                self.dof_blocks,
                self.ss_blocks,
                self.mss_blocks,
                self.f_blocks,
                self.p_blocks,
            ],
            ["Error", self.dof_error, self.ss_error, self.mss_error, "", ""],
            ["Total", self.dof_total, self.ss_total, "", "", ""],
        ]

        for row in rows:
            table.add_row(row)

        return table
