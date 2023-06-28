import string
#MSG = b'Ilovecake'

#def encryption(msg):
#    ct = []
#    for char in msg:
#        print(char)
#        ct.append((123 * char + 18) % 256)
#    print(ct)
#    return bytes(ct)

#ct = encryption(MSG)
#print(ct)

MSG = "6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921"
MSG = bytes.fromhex(MSG)
print(MSG)
i = 0
c = []
for i in MSG:
    for j in range(256):
        if((123*j + 18 - i) % 256 == 0):
            c.append(j)
            break

print("".join(chr(s) for s in c))