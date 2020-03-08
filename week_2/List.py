data = [9,8,7,4,5,6,3,2,1,4,5,6,7,6,7]

print(len(data))

print("Insert 7")
data.insert(5,7)
print(data)

print("Append 10")
data.append(10)
print(data)

print("del")
del data[2:4]
print(data)

print("remove gia tri 10")
data.remove(10)
print(data)

print("Pop vi tri 8")
data.pop(8)
print(data)

print("Index 5")
print(data.index(5))

print("Count 7")
print(data.count(7))

print('Tang')
data.sort()
print(data)

print('Giam')
data.sort(reverse=True)
print(data)



