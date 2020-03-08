import math

def Median(data):
    data.sort()
    n = len(data)
    i = int(n/2)

    if n%2==1:
        return data[i+1]
    else:
        return (data[i]+data[i+1])/2

data = [95,60,70,900,100,200,500,500,503,600,1000,1200]

print(Median(data))