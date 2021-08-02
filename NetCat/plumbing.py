from pwn import remote
import re

def main():
    url, port = "jupiter.challenges.picoctf.org", 7480
    r = remote(url,port)
    haha = r.recvall().decode()
    flag = re.findall(r'picoCTF{.*?}', haha)[0]
    print(flag)
main()