def addZero (a):
    a = (a // 2) * 2
    return a

def addOne (a):
    a = ((a // 2) * 2) + 1
    return a

def getBit (a):
    a = a % 2
    return str(a)

def encodeChar (a):
    s = (ord(a.encode('cp1251')))
    return s

def decodeChar (s):
    if s > 127:
        s = chr(s + 848)
    else:
        s = chr(s)
    return s

def decToBin (a):
    s = '00000000'
    a = str(bin(a)[2:])
    s = s[:8 - len(a)] + a
    return s

def binToDec (a):
    s = '0b'+a
    s = int (s,2)
    return s

# encodeStr = ''
# decodeStr = ''
# decodeArr = []
# inpStr = input('Введите текст сообщения \n')
# for char in inpStr:
#     encodeStr += decToBin(encodeChar(char))
# print(encodeStr)
#
# count = 0
# for i in range(int(len(encodeStr) / 8)):
#     decodeArr.append(encodeStr[count:count+8])
#     count += 8
# print(decodeArr)
# for i in range(len(decodeArr)):
#     decodeArr[i] = binToDec(decodeArr[i])
# print(decodeArr)
#
# for i in decodeArr:
#     decodeStr += decodeChar(i)
# print(decodeStr)

