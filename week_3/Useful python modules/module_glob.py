import glob

#Get path with file end of .jpg
for name in  glob.glob('images/*.jpg'):
    print(name)

lst = glob.glob('images/*.jpg')
print(lst)
print(lst[0])