def mean(s):
    return sum(s) / len(s)

def deviation(s):
    sMean = mean(s)
    return [si - sMean for si in s]

def variance(s):
    N = len(s)
    sDeviation = deviation(s)
    return dot(sDeviation, sDeviation)/N

def standtard_deviation(s):
    return variance(s)**0.5

def dot(x, y):
    return sum(xi * yi for xi, yi in zip(x, y))

def cov(x, y):
    N = len(x)
    xDeviation = deviation(x)
    yDeviation = deviation(y)
    return dot(xDeviation, yDeviation)/N

def find_corr_x_y(x, y):
    stdarx = standtard_deviation(x)
    stdary = standtard_deviation(y)
    return cov(x, y) / (stdarx * stdary)

x = [7, 18, 29, 2, 10, 9, 9]
y = [1, 6, 12, 8, 6, 21, 10]
points = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]

print('Phương sai: ', variance(points))
print('Độ lệch chuẩn: ', standtard_deviation(points))
print('Độ tương đồng: ', find_corr_x_y(x,y))



