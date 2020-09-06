import stego
from PIL import Image

decodeStr = ''
decodeArr = []
length = 0

img = Image.open('encrypt.png')
w, h = img.size

for i in range(8):
    a, r, g, b = img.getpixel((i % w, i // w))
    decodeStr += str(g)
length = (stego.binToDec(decodeStr)) * 8
decodeStr = ''
for i in range(length):
    a, r, g, b = img.getpixel((i % w, i // w))
    decodeStr += str(r)

encodeStr = decodeStr
decodeStr = ''
count = 0
for i in range(int(len(encodeStr) / 8)):
    decodeArr.append(encodeStr[count:count+8])
    count += 8

for i in range(len(decodeArr)):
    decodeArr[i] = stego.binToDec(decodeArr[i])

for i in decodeArr:
    decodeStr += stego.decodeChar(i)
print(decodeStr)

