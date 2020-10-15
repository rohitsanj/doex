import numpy as np

from .utils import p_value, create_anova_table


class LatinSquare:
    def __init__(self, treatments_order, treatments_values):
        self.treatments = list()
        self.treatments_order = np.array(treatments_order)
        self.treatments_values = np.array(treatments_values)

        if self.treatments_order.shape != self.treatments_values.shape:
            raise ValueError("treatments_order and treatments_values must have same shape")

        self._validate_treatments_order()

        self.combined_data = np.dstack((self.treatments_order, self.treatments_values))
        n_rows, n_cols = self.treatments_values.shape

        N = 0
        for entry in self.treatments_values:
            N += len(entry)

        self.treatments_data = self._create_treatments_data()

        self.correction_factor = np.square(np.sum(self.treatments_values)) / N

        # Calculate Sum of Squares
        self.row_totals = np.sum(self.treatments_values, axis=1)
        self.ss_rows = np.sum(np.square(self.row_totals)) / n_cols
        self.ss_rows = self.ss_rows - self.correction_factor

        self.column_totals = np.sum(self.treatments_values, axis=0)
        self.ss_columns = np.sum(np.square(self.column_totals)) / n_rows
        self.ss_columns = self.ss_columns - self.correction_factor

        self.treatment_totals = np.sum(self.treatments_data, axis=1)
        self.ss_treatments = np.sum(np.square(self.treatment_totals)) / len(self.treatments)
        self.ss_treatments = self.ss_treatments - self.correction_factor

        self.ss_total = np.sum(np.square(self.treatments_values)) - self.correction_factor

        self.ss_error = self.ss_total - (self.ss_rows + self.ss_columns + self.ss_treatments)

        # Calculate Degrees of Freedom
        self.dof_rows = n_cols - 1
        self.dof_columns = n_rows - 1
        self.dof_treatments = len(self.treatments) - 1
        self.dof_total = N - 1
        self.dof_error = self.dof_total - (self.dof_rows + self.dof_columns + self.dof_treatments)

        # Calculate Mean Sum of Squares
        self.mss_rows = self.ss_rows / self.dof_rows
        self.mss_columns = self.ss_columns / self.dof_columns
        self.mss_treatments = self.ss_treatments / self.dof_treatments
        self.mss_error = self.ss_error / self.dof_error

        self.f_rows = self.mss_rows / self.mss_error
        self.f_columns = self.mss_columns / self.mss_error
        self.f_treatments = self.mss_treatments / self.mss_error

        self.p_rows = p_value(self.f_rows, self.dof_rows, self.dof_error)
        self.p_columns = p_value(self.f_columns, self.dof_columns, self.dof_error)
        self.p_treatments = p_value(self.f_treatments, self.dof_treatments, self.dof_error)

        # Display results
        self.table = self._create_table()
        print(self.table)

    def _validate_treatments_order(self):
        for row in self.treatments_order:
            self.treatments = list(set(self.treatments + list(row)))

        if len(self.treatments) != len(self.treatments_order[0]):
            raise ValueError("Symbols in treatments_order are not same across all rows")

    def _create_treatments_data(self):
        treatments_data = []
        for treatment in self.treatments:
            temp = []
            for row in self.combined_data:
                for data in row:
                    if treatment == data[0]:
                        temp.append(float(data[1]))
            treatments_data.append(temp)

        return treatments_data

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
                "Rows",
                self.dof_rows,
                self.ss_rows,
                self.mss_rows,
                self.f_rows,
                self.p_rows,
            ],
            [
                "Columns",
                self.dof_columns,
                self.ss_columns,
                self.mss_columns,
                self.f_columns,
                self.p_columns,
            ],
            ["Error", self.dof_error, self.ss_error, self.mss_error, "", ""],
            ["Total", self.dof_total, self.ss_total, "", "", ""],
        ]

        for row in rows:
            table.add_row(row)

        return table
