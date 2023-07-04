import owiener
from gmpy2 import mpz, invert, powmod

f = open(".\input.txt")
s = []
s = f.readlines()
f.close()
t = []
for i in range(0,len(s),3):
    N = s[i].strip('N = ')
    e = s[i+1].strip('e = ')
    N = int(N,16)
    e = int(e,16)
    d = owiener.attack(e,N)
    if(d != None):
        t.append(d)

c = []
for i in t:
    s = hex(i)
    c.append(s.strip('0x'))

print("".join(bytes.fromhex(s).decode() for s in c))