file_path = "hello_world.txt"
file_handle = open(file_path, 'r')

data = file_handle.read()
print(type(data))
print('---------------')
print(data)

file_handle.close()