import gzip

#Create
data = 'plain text'
f = open('file.txt.gzip', 'wb')
f.write(data.encode())
f.close()

#Read
f = open('file.txt.gzip', 'rb')
data = f.read()
print(data.decode())
f.close()