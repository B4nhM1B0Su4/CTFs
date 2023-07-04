import binascii
import base64

h = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
format = b"crypto{"
key = [h1 ^ h2 for (h1,h2) in zip(h,format)] + [ord("y")] #y is missing at the end
flag = []
for i in range(len(h)):
	flag.append(h[i] ^ key[i % len(key)])
	

flag = "".join(chr(i) for i in flag)
print(flag)