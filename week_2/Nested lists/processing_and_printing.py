a = [[1, 2, 3], [4, 5, 6, 7], [1, 2]]

# Print a two-dimentional array
"""
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
"""

for row in a:
    for elem in row:
        print(elem, end=' ')
    print()

#To ouput a single line
for row in a:
    print(' '.join([str(elem) for elem in row]))

#Sum
s = 0
for row in a:
    s += sum([elem for elem in row])

print(s)