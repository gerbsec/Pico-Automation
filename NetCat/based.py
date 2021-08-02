import pwn
import re
import binascii


def binary_decode(binary):
    binary = binary.replace(" ", "")
    bin = '0b'+str(binary)
    n = int(bin, 2)
    decode = binascii.unhexlify('%x' % n)
    return decode


def octal_decode(octal):
    octal_converted = ""
    for octal_char in octal.split():
        octal_converted += chr(int(octal_char, 8))
    return bytes(octal_converted, 'utf')


def hex_decode(hex):
    hex_decoded = bytearray.fromhex(hex).decode()
    hex_decoded = bytes(hex_decoded, 'utf')
    return hex_decoded


def get_encrypted_word(received):
    word_encoded = (re.findall(r'\bthe\b(.*)\bas\b', received))
    return word_encoded[0]


def main():
    url, port = "jupiter.challenges.picoctf.org", 29221
    endbit = b'\r\n'
    r = pwn.remote(url, port)
    encrypted_binary = get_encrypted_word(r.recv().decode())
    binary = (binary_decode(encrypted_binary))
    r.send(binary + endbit)
    encrypted_octal = get_encrypted_word(r.recv().decode())
    octal = octal_decode(encrypted_octal)
    r.send(octal+endbit)
    encrypted_hex = get_encrypted_word(r.recv().decode())
    hex = hex_decode(encrypted_hex)
    r.send(hex + endbit)
    flag = re.findall(r'picoCTF{.*?}', r.recv().decode())[0]
    print(flag)
    r.close()


main()
