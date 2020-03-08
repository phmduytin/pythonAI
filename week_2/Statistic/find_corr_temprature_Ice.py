from matplotlib import pyplot as plt


def mean(s):
    return sum(s) / len(s)


def deviation(s):
    sMean = mean(s)
    return [si - sMean for si in s]


def variance(s):
    N = len(s)
    sDeviation = deviation(s)
    return dot(sDeviation, sDeviation) / N


def standtard_deviation(s):
    return variance(s) ** 0.5


def dot(x, y):
    return sum(xi * yi for xi, yi in zip(x, y))


def cov(x, y):
    N = len(x)
    xDeviation = deviation(x)
    yDeviation = deviation(y)
    return dot(xDeviation, yDeviation) / N


def find_corr_x_y(x, y):
    stdarx = standtard_deviation(x)
    stdary = standtard_deviation(y)
    return cov(x, y) / (stdarx * stdary)


Temperature = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]

Ice_Cream_Sales = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]

corr = str(find_corr_x_y(Temperature, Ice_Cream_Sales))

plt.scatter(Temperature, Ice_Cream_Sales)
plt.title(corr)
plt.xlabel('Temperature')
plt.ylabel('Ice_Cream_Sales')
plt.legend(loc='best')

plt.show()
