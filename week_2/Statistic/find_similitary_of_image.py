import math
import numpy as np
from PIL import Image


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


# Load ảnh và chuyển vê list:
image1 = Image.open('images/img1.png')
image2 = Image.open('images/img2.png')
image3 = Image.open('images/img3.png')
image4 = Image.open('images/img4.png')

image1_list = np.asarray(image1).flatten().tolist()
image2_list = np.asarray(image2).flatten().tolist()
image3_list = np.asarray(image3).flatten().tolist()
image4_list = np.asarray(image4).flatten().tolist()

print('Hệ số tương quan img1 vs img2: ', find_corr_x_y(image1_list, image2_list))
print('Hệ số tương quan img1 vs img3: ', find_corr_x_y(image1_list, image3_list))
print('Hệ số tương quan img1 vs img4: ', find_corr_x_y(image1_list, image4_list))

image4.show()