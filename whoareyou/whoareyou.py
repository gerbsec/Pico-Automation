import requests
import re

def main():
    url = "http://mercury.picoctf.net:46199/"
    header = {
        "User-Agent": "PicoBrowser",
        "Referer": "http://mercury.picoctf.net:46199/",
        "Date": "2018", "Dnt": "1",
        "X-Forwarded-For": "212.107.154.192",
        "Accept-Language": "sv-SE"
    }
    r = requests.get(url, headers=header)
    flag = re.findall("picoCTF{.*}", r.text)[0]
    print(flag)


main()
