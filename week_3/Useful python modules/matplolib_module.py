import matplotlib.pyplot as plt
import math


def linear_space(start, stop, num=10):
    num = int(num)
    start = start * 1.
    stop = stop * 1.

    assert (num > 1), 'number should be greater than 1'

    step = (stop - start) / num

    res = []
    for i in range(num):
        res.append(start + step * i)
    return res


'''
x_data = [0, 1, 2, 3, 4]
y_data = [1, 5, 4, 6, 4]

plt.plot(x_data, y_data)
plt.xlabel("x value")
plt.ylabel('y value')
plt.show()
'''


# print(linear_space(1, 10, 1))

# use linear_space draw tanh funtion

def tanh_funtion(data):
    return [(2 / (1 + math.exp(-2 * x)) - 1) for x in data]


def tanh_derivative(data):
    return [1 - x ** 2 for x in data]


data = linear_space(-5., 5., 100)
data_tanh = tanh_funtion(data)
data_dtanh = tanh_derivative(data_tanh)

fig, ax = plt.subplots(figsize=(10, 5))
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


ax.plot(data, data_tanh, color='red', linewidth=3, label="tanh")
ax.plot(data, data_dtanh, color='green', linewidth=3, label='tanh derivative')
ax.legend(loc='best')
plt.show()