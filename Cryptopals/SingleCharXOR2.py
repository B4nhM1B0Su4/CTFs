import string
file = open("./60Lines.txt", "r")
t2 = string.printable
t2 = t2.encode()
count = 0
while True:
	t1 = file.readline()
	if(t1 == ""): break
	t1 = bytes.fromhex(t1)
	for c in t2:
		t = []
		for i in range(len(t1)):
			t.append(t1[i] ^ c)
		s = "".join(chr(k) for k in t)
		if(all(t in string.printable for t in s)):
			print(chr(c)+": ", s)