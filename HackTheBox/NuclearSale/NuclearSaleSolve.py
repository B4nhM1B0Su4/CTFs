s1 = bytes.fromhex("6b65813f4fe991efe2042f79988a3b2f2559d358e55f2fa373e53b1965b5bb2b175cf039")
s2 = bytes.fromhex("fd034c32294bfa6ab44a28892e75c4f24d8e71b41cfb9a81a634b90e6238443a813a3d34")
s3 = bytes.fromhex("de328f76159108f7653a5883decb8dec06b0fd9bc8d0dd7dade1f04836b8a07da20bfe70")

k = []
i = 0
for c in s3:
    k.append(c ^ s2[i])
    i += 1

k = ''.join('{:02x}'.format(x) for x in k)
print(k)
k = bytes.fromhex(k)
m = []
i = 0

for c in k:
    m.append(c ^ s1[i])
    i += 1

print("".join(chr(c) for c in m))