from PIL import Image, ImageDraw

w = 200
h = 200
shape = [(20,20),w-20,h-20]

img = Image.new("RGB",(w,h))
img1 = ImageDraw.Draw(img)  
img1.rectangle(shape, fill ="red")
img.show()

def setfp(num,size):
    s = num//size
size = 25
codedata = []
for i in range(size*size):
    codedata.append(0)
