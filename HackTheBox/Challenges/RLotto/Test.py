import time
import random
outputs = []

print("START THIS AT THE SAME TIME YOU'RE CONNECTING, YOU'VE GOT A ~5 SECOND WINDOW")

for seed in range(int(time.time()-5),int(time.time()+5)):
	while True:
		extracted = []
		next_five = []


random.seed(seed)

# First extraction
while len(extracted) < 5:
	r = random.randint(1, 90)
	if(r not in extracted):
		extracted.append(str(r))

# Next extraction
solution = ""
while len(next_five) < 5:
	r = random.randint(1, 90)
	if(r not in next_five):
		next_five.append(str(r))
		solution += str(r) + " "
		solution = solution.strip()
		break

print(f"{seed}\t{extracted} {next_five}")
outputs.append(" ".join(extracted) + "," + " ".join(next_five))

first = int(input("ENTER FIRST NUMBER >"))

for i in outputs:
	if int(i.split(" ")[0]) == first: print(i)