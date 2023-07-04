h1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
h1 = h1.encode()
h2 = "ICE"
h2 = h2.encode()
h = bytearray()

for i in range(len(h1)):
	h.append(h1[i] ^ h2[i % len(h2)])

print(h.hex())