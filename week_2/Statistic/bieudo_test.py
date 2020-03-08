import numpy as np
from matplotlib import pyplot as plt

Lan_chay = [1, 2, 3, 4, 5, 6]

So_giay = [25.1, 21.2, 17.9, 23.0, 24.6, 19.5]
phut = [27, 22, 26, 26, 29, 25]

index = np.arange(6)
width = 0.3

plt.bar(index, So_giay, width = 0.3, color = 'green', label='giay')
plt.bar(index + width, phut, width = 0.3, color = 'red', label ='phut')
plt.xlabel("Số lần")
plt.ylabel("Số giây")
plt.title("Thống kê")
plt.xticks(index + width/2, Lan_chay)

plt.legend(loc = 'best')

#print(plt)

plt.show()
