import re
import requests

url = "https://jupiter.challenges.picoctf.org/static/495d43ee4a2b9f345a4307d053b4d88d/file"
r = requests.get(url)
filename = 'file'
with open(filename, 'wb') as output_file:
    output_file.write(r.content)
opened = open(filename)
flag = re.findall("picoCTF{.*?}", opened.read())[0]
print(flag)