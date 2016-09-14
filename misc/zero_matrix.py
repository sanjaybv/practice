import numpy as np

def set_zero(matrix):
    (num_rows, num_cols) = matrix.shape
    zero_rows = set()
    zero_cols = set()

    for row_index, row in enumerate(matrix):
        for col_index, number in enumerate(row):
            if number == 0:
                zero_rows.add(row_index)
                zero_cols.add(col_index)

    for row_index in zero_rows:
        matrix[row_index, :] = np.zeros(num_cols)

    for col_index in zero_cols:
        matrix[:, col_index] = np.zeros(num_rows)

matrix = np.array([
            [1, 2, 3, 4],
            [5, 0, 6, 7],
            [8, 9, 1, 2],
            [3, 4, 5, 0]
        ])

print matrix
set_zero(matrix)
print matrix
