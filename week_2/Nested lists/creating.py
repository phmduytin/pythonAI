n = 3
m = 4
"""
#Wrong:
a = [[0] * m] * n

a[1][2] = 5

for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
"""

# 1
"""a = []
for i in range(n):
    a.append([0]*m)
"""
# 2

a = [[0] * m for i in range(n)]

a[1][2] = 5

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
    # print(' '.join([str(elem) for elem in row]))
