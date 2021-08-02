import html
import requests
import re


def download_files():
    name = ['a', 'b']
    for letter in name:
        url = f'https://s3-eu-west-1.amazonaws.com/md5collisions/{letter}.php'
        r = requests.get(url)
        filename = f'{letter}.pdf'
        with open(filename, 'wb') as output_file:
            output_file.write(r.content)


def upload_files():
    url = 'http://mercury.picoctf.net:55343/index.php'

    files = {'file1': ('a.pdf', open('a.pdf', 'rb'), 'application/pdf'),
             'file2': ('b.pdf', open('b.pdf', 'rb'), 'application/pdf')}
    data = {'submit': 'Upload'}
    r = requests.post(url, files=files, data=data)
    flag = re.findall("picoCTF{.*?}", html.unescape(r.text))[0]
    print(flag)


download_files()
upload_files()
