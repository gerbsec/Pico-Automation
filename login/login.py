import requests
import re
import base64
url = "https://login.mars.picoctf.net/index.js"
r = requests.get(url)

flag = re.findall(r'"(.*?)"', r.text)[-2]
ctf = base64.b64decode(flag + "==").decode()
print(ctf)