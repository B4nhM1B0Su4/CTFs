import base64
b = input()
b = bytes.fromhex(b)
print(base64.b64encode(b))