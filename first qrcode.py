import qrcode

data = "hallo"

img = qrcode.make(data)

img.save("testqrcode3.png")