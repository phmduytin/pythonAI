import math

E = 1

N = 100000

gt = 1

for i in range(1,N):
    gt = gt * i
    E = E + 1/gt

print(E)