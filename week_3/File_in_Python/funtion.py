
#OS
import os

file_path = "write_file.txt"

if os.path.exists(file_path):
    filehandle = open(file_path, 'a')

else:
    filehandle = open(file_path, 'w')

text3 = "line os \n"
#filehandle.write(text3)

filehandle.close()

#Split()
line1 = '001,John,22-12-1996'
infor = line1.split(',')
print(infor[2])

#Join()
line2 = ['001','John','22-12-1996']
infor = ','.join(line2)
print(infor)
