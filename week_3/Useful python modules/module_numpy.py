import numpy as np

# array
a = np.array([1, 2, 3])
print(type(a))
a[1] = 10
print(a.shape)

# two dimension
a = np.array([[1, 2, 3, 6], [3, 4, 5, 3]])
print(a[0, 1])
print(a.shape)

# create two dimesion
# unsigned int 8 bit
height = 4
width = 5
image = np.zeros((height, width), np.uint8)
image[1][1] = 1000
print(image)