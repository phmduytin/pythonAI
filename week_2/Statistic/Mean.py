import math

def mean(data):
    N = len(data)
    S = sum(data)
    return S/N

data = [95,60,70,900,100,200,500,500,503,600,1000,1200]

print(mean(data))