import math
import random

N = 1000000
NT = 0;

for _ in range(N):
    x = random.random()*2 - 1
    y = random.random()*2 - 1
    if x*x+y*y<=1:
        NT = NT+1

print(4*NT/N)

