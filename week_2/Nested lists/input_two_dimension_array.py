print("n = ")
n = int(input())

a = []

print("Input: ")

for i in range(n):
    a.append([int(j) for j in input().split()])

for row in a:
    for elem in row:
        print(elem, end=' ')
    print()

