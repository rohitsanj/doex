import numpy as np

from .utils import p_value, create_anova_table


class RandomizedCompleteBlockDesign:
    def __init__(self, data):
        self.data = np.array(data)

        n_treatments, n_blocks = self.data.shape

        if hasattr(self, "num_missing"):
            num_missing = self.num_missing
        else:
            num_missing = 0

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
        self.dof_error = self.dof_total - (self.dof_treatments + self.dof_blocks + num_missing)

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


TwoWayANOVA = RandomizedCompleteBlockDesign


class RandomizedCompleteBlockDesign_MissingValues(RandomizedCompleteBlockDesign):
    def __init__(self, data):
        self.data = np.array(data)

        n_treatments, n_blocks = self.data.shape

        self.num_missing = np.count_nonzero(np.isnan(self.data))
        missing_locations = np.argwhere(np.isnan(self.data))
        self.handle_missing(self.data, missing_locations)

        print("Data after adjusting for {} missing value(s)".format(self.num_missing))
        print(self.data)

        # Continue with RCBD analysis
        super().__init__(self.data)

    def handle_missing(self, data, locations):
        if len(locations) == 1:
            return self._missing_1_value(data, locations[0])
        elif len(locations) == 2:
            return self._missing_2_values(data, locations)
        else:
            raise Exception("Data must have either 1 or 2 missing values")

    def _missing_1_value(self, data, location):
        k, r = data.shape  # k treatments, r replications
        i, j = location

        G = np.nansum(data)
        treatments_sum = np.nansum(data[i, :])
        blocks_sum = np.nansum(data[:, j])

        self.data[i, j] = (r * blocks_sum + k * treatments_sum - G) / ((r - 1) * (k - 1))

    def _missing_2_values(self, data, locations):
        k, r = data.shape  # k treatments, r replications

        y1_loc, y2_loc = locations
        i, j = y1_loc
        m, j_1 = y2_loc

        G = np.nansum(data)
        Ti = np.nansum(data[i, :])
        Tm = np.nansum(data[m, :])
        Bj = np.nansum(data[:, j])
        Bj_1 = np.nansum(data[:, j_1])

        y1_estimate = ((k - 1) * (r - 1) * (k * Ti + r * Bj - G) - (k * Tm + r * Bj_1 - G)) / (
            np.square(r - 1) * np.square(k - 1) - 1
        )

        y2_estimate = ((k - 1) * (r - 1) * (k * Tm + r * Bj_1 - G) - (k * Ti + r * Bj - G)) / (
            np.square(r - 1) * np.square(k - 1) - 1
        )

        self.data[y1_loc[0], y1_loc[1]] = y1_estimate
        self.data[y2_loc[0], y2_loc[1]] = y2_estimate
