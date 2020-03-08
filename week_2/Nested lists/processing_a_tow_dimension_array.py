print("n = ")
n = int(input())

a = []

# Example 1

"""
#Solution 1:
for i in range(n):
    row = []
    for j in range(n):
        if i==j:
            row.append(1)
        elif i>j:
            row.append(2)
        else:
            row.append(0)
    a.append(row)
"""

"""
#Solution 2:
for i in range(n):
    row = []
    for j in range(i):
        row.append(2)
    row.append(1)
    for j in range(i+1,n):
        row.append(0)
    a.append(row)
"""

#Solution 3: Very great (y)
#for i in range(n):
#    a.append([2]*i+[1]+[0]*(n-i-1))

#or

#a = [0]*n
a = [[2]*i+[1]+[0]*(n-1-i) for i in range(n)]

for row in a:
    print(' '.join([str(elem) for elem in row]))

