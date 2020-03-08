from collections import Counter

def Modes(data):
    c = Counter(data)
    num_freq = c.most_common()
    max_count = num_freq[0][1]
    modes = []
    for num in num_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes

data = [7,6,9,6,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10]

print("Modes của dãy data: ", Modes(data))
