import numpy as np
from numpy.linalg import inv


def covariance(X, Y, show_steps=False):
    X = np.array(X)
    Y = np.array(Y)
    show_steps

    if len(X) != len(Y):
        raise ValueError("Both lists must have same number of values")

    N = len(X)

    x_mean = np.average(X)
    y_mean = np.average(Y)

    s_xy = np.sum((X - x_mean) * (Y - y_mean)) / (N - 1)

    s_x = np.sqrt((np.sum(np.square(X)) - N * (x_mean ** 2)) / (N - 1))
    s_y = np.sqrt((np.sum(np.square(Y)) - N * (y_mean ** 2)) / (N - 1))

    r_xy = s_xy / (s_x * s_y)

    print("Covariance: ", "{:.4f}".format(s_xy))
    print("Correlation coefficient: ", "{:.4f}".format(r_xy))


def covariance_matrix(data, show_steps=False):

    data = np.transpose(np.array(data))
    f = data.shape[1]
    N = data.shape[0]
    S = (data.T @ (np.identity(N) - np.ones(N) / N) @ data) / (N - 1)

    print("Mean vector: ")
    print(np.average(data, axis=0))
    print("Covariance Matrix: ")
    print(S)

    Ds = np.identity(f)
    Ds[np.diag_indices(f)] = np.sqrt(np.diagonal(S))

    print("Ds: ")
    print(Ds)

    R = inv(Ds) @ S @ inv(Ds)

    print("Correlation Matrix: ")
    print(R)
