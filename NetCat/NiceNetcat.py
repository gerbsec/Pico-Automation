from pwn import remote


def main():
    url, port = 'mercury.picoctf.net', 21135
    r = remote(url, port)
    values = r.recvall().decode()
    flag = ""
    for i in values.split():
        flag += chr(int(i))
    print(flag, end='')


main()
