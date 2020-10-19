import numpy as np

from .utils import p_value, create_anova_table


class GraecoLatinSquare:
    def __init__(self, latin, greek, treatments_values):

        self.greek = np.array(greek)
        self.latin = np.array(latin)
        self.treatments_values = np.array(treatments_values)

        if (
            self.greek.shape != self.treatments_values.shape
            or self.latin.shape != self.treatments_values.shape
        ):
            raise ValueError("All inputs must have same shape")

        self.greek_treatments_list = self._get_treatments_list(self.greek)
        self.latin_treatments_list = self._get_treatments_list(self.latin)

        combined_greek_data = np.dstack((self.greek, self.treatments_values))
        combined_latin_data = np.dstack((self.latin, self.treatments_values))

        n_rows, n_cols = self.treatments_values.shape
        p = self.treatments_values.shape[0]

        num_treatments = p
        N = p ** 2

        self.greek_treatments_data = self._create_treatments_data(
            combined_greek_data, self.greek_treatments_list
        )
        self.latin_treatments_data = self._create_treatments_data(
            combined_latin_data, self.latin_treatments_list
        )

        self.correction_factor = np.square(np.sum(self.treatments_values)) / N

        # Calculate Sum of Squares

        # Rows
        self.row_totals = np.sum(self.treatments_values, axis=1)
        self.ss_rows = np.sum(np.square(self.row_totals)) / n_cols
        self.ss_rows = self.ss_rows - self.correction_factor

        # Columns
        self.column_totals = np.sum(self.treatments_values, axis=0)
        self.ss_columns = np.sum(np.square(self.column_totals)) / n_rows
        self.ss_columns = self.ss_columns - self.correction_factor

        # Greek
        self.greek_treatment_totals = np.sum(self.greek_treatments_data, axis=1)
        self.ss_greek_treatments = np.sum(np.square(self.greek_treatment_totals)) / num_treatments
        self.ss_greek_treatments = self.ss_greek_treatments - self.correction_factor

        # Latin
        self.latin_treatment_totals = np.sum(self.latin_treatments_data, axis=1)
        self.ss_latin_treatments = np.sum(np.square(self.latin_treatment_totals)) / num_treatments
        self.ss_latin_treatments = self.ss_latin_treatments - self.correction_factor

        self.ss_total = np.sum(np.square(self.treatments_values)) - self.correction_factor

        self.ss_error = self.ss_total - (
            self.ss_rows + self.ss_columns + self.ss_greek_treatments + self.ss_latin_treatments
        )

        # Calculate Degrees of Freedom
        self.dof_rows = p - 1
        self.dof_columns = p - 1
        self.dof_greek_treatments = p - 1
        self.dof_latin_treatments = p - 1
        self.dof_total = N - 1
        self.dof_error = self.dof_total - (
            self.dof_rows + self.dof_columns + self.dof_greek_treatments + self.dof_latin_treatments
        )

        # Calculate Mean Sum of Squares
        self.mss_rows = self.ss_rows / self.dof_rows
        self.mss_columns = self.ss_columns / self.dof_columns
        self.mss_greek_treatments = self.ss_greek_treatments / self.dof_greek_treatments
        self.mss_latin_treatments = self.ss_latin_treatments / self.dof_latin_treatments
        self.mss_error = self.ss_error / self.dof_error

        self.f_rows = self.mss_rows / self.mss_error
        self.f_columns = self.mss_columns / self.mss_error
        self.f_greek_treatments = self.mss_greek_treatments / self.mss_error
        self.f_latin_treatments = self.mss_latin_treatments / self.mss_error

        self.p_rows = p_value(self.f_rows, self.dof_rows, self.dof_error)
        self.p_columns = p_value(self.f_columns, self.dof_columns, self.dof_error)
        self.p_greek_treatments = p_value(
            self.f_greek_treatments, self.dof_greek_treatments, self.dof_error
        )
        self.p_latin_treatments = p_value(
            self.f_latin_treatments, self.dof_latin_treatments, self.dof_error
        )

        # Display results
        self.table = self._create_table()
        print(self.table)

    @staticmethod
    def _get_treatments_list(treatments_order):
        treatments = list()
        for row in treatments_order:
            treatments = list(set(treatments + list(row)))

        if len(treatments) != len(treatments_order[0]):
            raise ValueError("Symbols in greek are not same across all rows")

        return treatments

    @staticmethod
    def _create_treatments_data(combined_data, treatments_list):
        treatments_data = []
        for treatment in treatments_list:
            temp = []
            for row in combined_data:
                for data in row:
                    if treatment == data[0]:
                        temp.append(float(data[1]))
            treatments_data.append(temp)

        return treatments_data

    def _create_table(self):
        table = create_anova_table()

        rows = [
            [
                "Latin treatments",
                self.dof_latin_treatments,
                self.ss_latin_treatments,
                self.mss_latin_treatments,
                self.f_latin_treatments,
                self.p_latin_treatments,
            ],
            [
                "Greek treatments",
                self.dof_greek_treatments,
                self.ss_greek_treatments,
                self.mss_greek_treatments,
                self.f_greek_treatments,
                self.p_greek_treatments,
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
