n = 4
a = [[1 for j in range(n)] for i in range(n)]

for row in a:
    print(' '.join([str(elem) for elem in row]))

