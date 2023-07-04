pt1 = b"hey let's rob the bank at midnight tonight!"
c1 = "4fd098298db95b7f1bc205b0a6d8ac15f1f821d72fbfa979d1c2148a24feaafdee8d3108e8ce29c3ce1291"
h1 = bytes.fromhex(c1)
c = []
k = 0
for i in pt1:
    c.append(h1[k] ^ i)
    k += 1

t2 = ''.join('{:02x}'.format(x) for x in c)

h2 = bytes.fromhex(t2)
c2 = bytes.fromhex("41d9806ec1b55c78258703be87ac9e06edb7369133b1d67ac0960d8632cfb7f2e7974e0ff3c536c1871b")
c = []
k = 0
for i in c2:
    c.append(i ^ h2[k])
    k += 1

print("".join(chr(s) for s in c))