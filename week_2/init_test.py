import math

def Mean(data):
    s = sum(data)
    n = len(data)
    return s / n


def Deviation(data):
    SMean = Mean(data)
    return [S_i - SMean for S_i in data]


def dot(x, y):
    return sum(xi * yi for xi, yi in zip(x, y))


def Variance(data):
    sDeviation = Deviation(data)
    return dot(sDeviation, sDeviation) / len(data)


def standard_deviation(data):
    return Variance((data)) ** 0.5


def find_corr_x_y(x, y):
    xDeviation = Deviation(x)
    yDeviation = Deviation(y)
    cov = dot(xDeviation, yDeviation) / len(x)
    return cov / (standard_deviation(x) * standard_deviation(y))


x = [7, 18, 29, 2, 10, 9, 9]
y = [1, 6, 12, 8, 6, 21, 10]

print('Hệ số tương quan: ', find_corr_x_y(x, y))
