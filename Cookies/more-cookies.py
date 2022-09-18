#HOMOMORPHIC ENCRYPTION
from base64 import b64decode, b64encode
import requests

def bitFlip(pos, bit, raw):
    list1 = list(raw)
    list1[pos] = chr(ord(list1[pos])^bit)
    raw = ''.join(list1)
    return b64encode(raw.encode("utf-8"))

ck = "AyQBlPHkrsXPafVw1WlOvmJYSkZRLED7JZ2sXyGbVqtpxhFlg6pzr2L14PHmA7wm2VGKhib+w1Qi/yFve32N4MJpel2poXl0s1PpGx3IkRFUcvKTFXeggJ5cMxW14vGx"
for i in range(128):
    for j in range(128):
        c = bitFlip(i, j, ck)
        c = c.decode("utf-8")
        cookies = {'auth_name':c}
        r = requests.get('http://mercury.picoctf.net:34962/', cookies=cookies)
        if "picoCTF" in r.text:
            print(r.text)
            break
