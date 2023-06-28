from gmpy2 import gcdext, invert
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long
import base64
f = open("key1.pem", 'r')
k1 = RSA.import_key(f.read())
f.close()
f = open("key2.pem", 'r')
k2 = RSA.import_key(f.read())
f.close()
e1 = k1.e
e2 = k2.e
n = k1.n
c1 = bytes_to_long(base64.b64decode("RBVdQw7Pllwb42GDYyRa6ByVOfzRrZHmxBkUPD393zxOcrNRZgfub1mqcrAgX4PAsvAOWptJSHbrHctFm6rJLzhBi/rAsKGboWqPAWYIu49Rt7Sc/5+LE2dvy5zriAKclchv9d+uUJ4/kU/vcpg2qlfTnyor6naBsZQvRze0VCMkPvqWPuE6iL6YEAjZmLWmb+bqO+unTLF4YtM1MkKTtiOEy+Bbd4LxlXIO1KSFVOoGjyLW2pVIgKzotB1/9BwJMKJV14/+MUEiP40ehH0U2zr8BeueeXp6NIZwS/9svmvmVi06Np74EbL+aeB4meaXH22fJU0eyL2FppeyvbVaYQ==",))
c2 = bytes_to_long(base64.b64decode("TSHSOfFBkK/sSE4vWxy00EAnZXrIsBI/Y6mGv466baOsST+qyYXHdPsI33Kr6ovucDjgDw/VvQtsAuGhthLbLVdldt9OWDhK5lbM6e0CuhKSoJntnvCz7GtZvjgPM7JDHQkAU7Pcyall9UEqL+W6ZCkiSQnK+j6QB7ynwCsW1wAmnCM68fY2HaBvd8RP2+rPgWv9grcEBkXf7ewA+sxSw7hahMaW0LYhsMYUggrcKqhofGgl+4UR5pdSiFg4YKUSgdSw1Ic/tug9vfHuLSiiuhrtP38yVzazqOZPXGxG4tQ6btc1helH0cLfw1SCdua1ejyan9l1GLXsAyGOKSFdKw=="))
_, u, v = gcdext(e1, e2)

if u < 0: # if u < 0, compute c1_inv
    c1_inv = invert(c1, n)
    M = (c1_inv**(-u) * c2**v) % n
else:
    c2_inv = invert(c2, n)
    M = (c2_inv**(-v) * c1**u) % n
s = str(M)
print(bytearray.fromhex(hex(M)[2:]).decode())