import math


def add_vector(vector1, vector2):
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]


def dot_product(vector1, vector2):
    return sum([v1 * v2 for v1, v2 in zip(vector1, vector2)])


def hadamard_product(vector1, vector2):
    return [v1 * v2 for v1, v2 in zip(vector1, vector2)]


def cosine_similary(vector1, vector2):
    sumxy = sum([v1 * v2 for v1, v2 in zip(vector1, vector2)])
    sumxx = sum([v1 * v2 for v1, v2 in zip(vector1, vector1)])
    sumyy = sum([v1 * v2 for v1, v2 in zip(vector2, vector2)])

    return sumxy / math.sqrt(sumxx * sumyy)


vector1 = [1, 2]
vector2 = [3, 4]

vector1 = [5, 3, 2, 7]
vector2 = [2, 9, 4, 1]

res = add_vector(vector1, vector2)
res = dot_product(vector1, vector2)
res = hadamard_product(vector1, vector2)
res = cosine_similary(vector1, vector2)

print(res)
