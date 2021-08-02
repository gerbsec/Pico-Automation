import requests
import re


def main():
    url = "http://mercury.picoctf.net:39698/"
    sites = ["index.html", "mycss.css", "robots.txt", ".htaccess", ".DS_Store"]
    flag = ""
    for i in sites:
        r = requests.get(url+i)
        if "flag:" in r.text:
            flag = re.findall("flag: (.{9})", r.text)
        elif "2:" in r.text:
            flag = flag + re.findall("2: (.{9})", r.text)
        elif "3:" in r.text:
            flag = flag + re.findall("3: (.{9})", r.text)
        elif "4:" in r.text:
            flag = flag + re.findall("4: (.{9})", r.text)
        elif "5:" in r.text:
            flag = flag + re.findall("5: (.{10})", r.text)
    x = "".join(flag)
    print(x)


main()
