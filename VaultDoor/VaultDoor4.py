

obf = [106, 85, 53, 116, 95, 52, 95, 98, '55', '6e', '43', '68', '5f', '30', '66', '5f', 142, 131, 164, 63 , 163, 137, 143, 61, '9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e']

for i in range(8):
    print(chr(obf[i]), end='')

for i in range(8, 16):
    print(bytes.fromhex(obf[i]).decode('ascii'), end='')

for i in range(16, 24):
    print(chr(int(str(obf[i]), 8)), end='')
for i in range(24, len(obf)):
    print(obf[i], end='')
