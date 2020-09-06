import stego
from PIL import Image

encodeStr = ''
decodeStr = ''
decodeArr = []
length = 0


img = Image.open('crypt.png')
w, h = img.size


inpStr = input('Введите текст сообщения \n')
length = stego.decToBin(len(inpStr))
for char in inpStr:
    encodeStr += stego.decToBin(stego.encodeChar(char))

for i in range(8):
    a, r, g, b = img.getpixel((i % w, i // w))
    k = stego.addOne(g) if length[i] == '1' else stego.addZero(g)
    img.putpixel((i % w, i // w), (a, r, k, b))

for i in range(len(encodeStr)):
    a, r, g, b = img.getpixel((i % w, i // w))
    k = stego.addOne(r) if encodeStr[i] == '1' else stego.addZero(r)
    img.putpixel((i % w, i // w), (a,k,g,b))

img.save('encrypt.png')




