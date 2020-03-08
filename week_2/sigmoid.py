import math

def sigmoid_function(data):
    result = []

    for i in data:
        result.append(1/(1+math.exp(-i)))

    return result

data = [1,5,-4,3,-2]

result = sigmoid_function(data)

print(result)