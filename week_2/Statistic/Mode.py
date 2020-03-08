from collections import Counter

"""
def Mode(data):
    c = Counter(data)
    Mode = c.most_common(1)
    return Mode[0][0]


data = [7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1,10]

print(Mode(data))

"""

s1 = [1, 1, 3, 3, 3, 4]
s2 = [1, 2, 3]
s3 = [1, 2, 2, 1]

def mode(data):
    counter = Counter(data);
    max_counter = max(counter.values())
    return [x for x, count in counter.items() if count == max_counter]

print(mode(s1))
print(mode(s2))
print(mode(s3))
