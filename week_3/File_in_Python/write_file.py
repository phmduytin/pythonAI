file_path = 'write_file.txt'
filehandle = open(file_path, 'w') # 'w' để tạo mới, 'a' để thêm tiếp

text1 = "line 1 \n"
text2 = 'line 2 \n'

filehandle.write(text1)
filehandle.write(text2)

filehandle.close()



