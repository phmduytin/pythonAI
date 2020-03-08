import math

points = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]

#Tính tổng bình phương
def sum_of_square(s):
    return sum(si * si for si, si in zip(s, s))

# Tính giá trị trung bình
def mean(s):
    return sum(s)/len(s)

# Độ lệch
def deviation(s):
    sMean = mean(s)
    return [si - sMean for si in s]

# Phương sai
def variance(s):
    n = len(s)
    d = deviation(s)
    return sum_of_square(d)/(n-1)

# Độ lệch chuẩn
def standard_deviation(s):
    return math.sqrt(variance(s))

print('Phương sai: ', variance(points))
print('Độ lệch chuẩn: ', standard_deviation(points))
