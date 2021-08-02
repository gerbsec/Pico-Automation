from pwn import remote
import re


def main():
    url, port = "jupiter.challenges.picoctf.org", 64287
    r = remote(url, port)
    response = r.recvall()
    flag = re.findall("picoCTF{.*?}", response.decode())[0]
    print(flag)


main()
