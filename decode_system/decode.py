import base64
import os

#enco = b"password = 12\n\ni = int(input('password :'))\nif password == i:\n    print('hello')\nelse:\n    print('fail')"
#enco_addr = b'/home/dadmehr/Documents/code/python/decode_system/main.py'
enco_addr = b'L2hvbWUvZGFkbWVoci9Eb2N1bWVudHMvY29kZS9weXRob24vZGVjb2RlX3N5c3RlbS9tYWluLnB5'
enco = b'cGFzc3dvcmQgPSAxMgoKaSA9IGludChpbnB1dCgncGFzc3dvcmQgOicpKQppZiBwYXNzd29yZCA9PSBpOgogICAgcHJpbnQoJ2hlbGxvJykKZWxzZToKICAgIHByaW50KCdmYWlsJyk='

#addr decode
deco_addr = base64.b64decode(enco_addr)
convetbytetostr_addr = deco_addr.decode('ascii')
# code decode
deco = base64.b64decode(enco)
convetbytetostr = deco.decode('ascii')

#crate file
path = convetbytetostr_addr
codefi = open(path,'w')
codefi.write(convetbytetostr)
codefi.close()

#open file
print(convetbytetostr_addr)
os.system('python3 '+convetbytetostr_addr)

"""
'r' - خواندن فایل
'w' - نوشتن فایل
'x' - ایجاد کردن و نوشتن فایل جدید
'a' - اضافه کردن محتوا به فایل
'+r' - برای خواندن و نوشتن
"""
