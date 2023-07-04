from gmpy2 import mpz, invert, powmod
c = mpz(int("2526512a4abf23fca755defc497b9ab",16))
e = mpz(257)
n = mpz(int("592f144c0aeac50bdf57cf6a6a6e135",16))
p = mpz(430535396861370041) #Got this after using Factordb
q = mpz(17209058493553260637) #Got this after using Factordb
phi = (p-1)*(q-1)
d = invert(e, phi) # e*d = 1 (mod phi(n)) => e*d = 1 + k*phi(n) <=> e*d - 1 = k*phi(n) (Use extended Euclidean to solve for k and d)
m = powmod(c, d, n)
h = hex(m)
b = bytearray.fromhex(h.strip('0x'))
print(b.decode('utf8'))