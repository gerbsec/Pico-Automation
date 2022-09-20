from base64 import b64decode
import urllib.parse

obf = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2"
print(urllib.parse.unquote(b64decode(obf).decode('utf-8')))
