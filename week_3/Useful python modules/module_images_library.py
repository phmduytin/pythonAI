from PIL import Image

img = Image.open('images/Sydney-Opera-House.jpg')

#print(img.format, img.size, img.mode)

#Convert to greyscale
#img = img.convert('L')

#out = img.resize((128,128))

out = img.rotate(45)

img.show()
out.show()
