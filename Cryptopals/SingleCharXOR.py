import string
t1 = input()
t1 = bytes.fromhex(t1)
t2 = string.printable
t2 = t2.encode()
print(t2)
for c in t2:
	t = []
	for i in range(len(t1)):
		t.append(t1[i] ^ c)
	s = "".join(chr(k) for k in t)
	print(chr(c)+": ", s)
	
