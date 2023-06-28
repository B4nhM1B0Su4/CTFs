import math
from random import randint, seed
from time import time, process_time

strchr = lambda x: chr(x) # Convert number to char
strbyt = lambda x, y=0: ord(x[y]) #Convert string char to byte
bitlst = lambda x, y: x << y # Shift Left
bitrst = lambda x, y: x >> y # Shift Right
bitext = lambda x, y, z=1: bitrst(x, y) & int(math.pow(2, z) - 1) # Extend bits
bitxor = lambda x, y: x ^ y # XOR
bitbor = lambda x, y: x | y # OR
btest = lambda x, y: (x & y) != 0 # x AND y not equal 0
mthrnd = lambda x, y: randint(x, y) # random int from x -> y
mthrsd = lambda x: seed(x)
osltim = lambda: int(time())
oslclk = lambda: process_time()

FL_NEGATE = bitlst(1, 1) # 2
FL_UNUSED3 = bitlst(1, 2) # 4
FL_XORBY6B = bitlst(1, 3) # 8
FL_XORBY3E = bitlst(1, 4) # 16
FL_UNUSED2 = bitlst(1, 5) # 32
FL_SWAPBYTES = bitlst(1, 6) # 64
FL_UNUSED1 = bitlst(1, 7) # 128

currtime = osltim()
while True:
    if osltim() - currtime != 0:
        break

mthrsd(osltim() + oslclk() * 1000)


def ValidateChar(char):
    if type(char) is str and len(char) == 1:
        char = strbyt(char)
    return char


def GenerateFlag():
    finalflag = 0
    if mthrnd(0, 1) == 1:
        finalflag = bitbor(finalflag, FL_SWAPBYTES)
    if mthrnd(0, 1) == 1:
        finalflag = bitbor(finalflag, FL_NEGATE)
    if mthrnd(0, 1) == 1:
        finalflag = bitbor(finalflag, FL_XORBY6B)
    if mthrnd(0, 1) == 1:
        finalflag = bitbor(finalflag, FL_XORBY3E)
    if mthrnd(0, 1) == 1:
        finalflag = bitbor(finalflag, FL_UNUSED3)
    if mthrnd(0, 1) == 1:
        finalflag = bitbor(finalflag, FL_UNUSED2)
    if mthrnd(0, 1) == 1:
        finalflag = bitbor(finalflag, FL_UNUSED1)

    return finalflag


def CheckFlag(f, flag): # Check if f AND flag != 0
    return btest(f, flag)


def ESwapChar(char):
    char = ValidateChar(char)
    THIS_MSB = bitext(char, 4, 4)# First 4 bits of number
    THIS_LSB = bitext(char, 0, 4)# Last 4 bits of number

    return strchr(bitbor(bitxor(THIS_MSB, 0x0D), bitxor(bitlst(THIS_LSB, 4), 0xB0)))

def EDeSwapChar(char):
    char = ValidateChar(char)
    THIS_MSB = bitext(char, 4, 4)
    THIS_LSB = bitext(char, 0, 4)

    return strchr(bitbor(bitxor(bitlst(THIS_LSB, 4), 0xD0), bitxor(THIS_MSB, 0x0B)))


def XorBy6B(char):
    char = ValidateChar(char)

    return strchr(bitxor(char, 0x6B)) # char XOR 107


def XorBy3E(char):
    char = ValidateChar(char)

    return strchr(bitxor(char, 0x3E)) # char XOR 62


def NegateChar(char):
    char = ValidateChar(char)

    return strchr(255 - char)


FLAGS = []
CHARS = []


def AppendFlag(flag):
    FLAGS.append(strchr(bitxor(flag, 0x4A)))


def EncryptCharacter(char):
    char = ValidateChar(char) # Check if char is str
    flag = GenerateFlag() # Generate random number

    if CheckFlag(flag, FL_SWAPBYTES): # if flag AND FL_SWAPBYTES != 0 then Swap char
        #print(CheckFlag(flag, FL_SWAPBYTES))
        char = ESwapChar(char)
    if CheckFlag(flag, FL_NEGATE): # if flag AND FL_NEGATE != 0 then Negate char (Negate = 255 - char)
        #print(CheckFlag(flag, FL_NEGATE))
        char = NegateChar(char)
    if CheckFlag(flag, FL_XORBY6B): # if flag AND FL_XORBY6B then char XOR 6B
        #print(CheckFlag(flag, FL_XORBY6B))
        char = XorBy6B(char)
    if CheckFlag(flag, FL_XORBY3E): # if flag AND FL_XORBY3E != 0, then char XOR 3E
        #print(CheckFlag(flag, FL_XORBY3E))
        char = XorBy3E(char)

    return char, flag

def DecryptCharacter(char, flag):
    char = chr(char)
    flag = flag ^ 74
    if CheckFlag(flag, FL_XORBY3E):
        #print(CheckFlag(flag, FL_XORBY3E), 1)
        char = XorBy3E(char)
    if CheckFlag(flag, FL_XORBY6B):
        #print(CheckFlag(flag, FL_XORBY6B), 2)
        char = XorBy6B(char)
    if CheckFlag(flag, FL_NEGATE):
        #print(CheckFlag(flag, FL_NEGATE), 3)
        char = NegateChar(char)
    if CheckFlag(flag, FL_SWAPBYTES):
        #print(CheckFlag(flag, FL_SWAPBYTES), 4)
        char = EDeSwapChar(char)

    return char


def _Encrypt(string):
    print("char before:", string)
    for i in range(0, len(string)):
        char, flag = EncryptCharacter(strbyt(string, i))
        print("char:",ord(char))
        print("flag:",flag)

        if type(char) is int:
            char = strchr(char) # Convert number to character

        CHARS.append(char)
        AppendFlag(flag)


def Encrypt(string):
    _Encrypt(string)

    output = [f"{str(ord(v))} {str(ord(FLAGS[i]))}" for i, v in enumerate(CHARS)]
    return output
#    file = open("output.txt", "w")
#    file.write(' '.join(output))
#   file.close()

msg = [108,182,82,176,167,158,69,222,39,102,234,14,241,16,10,218,160,108,76,234,225,224,1,12,97,122,114,90,10,90,250,14,155,80,101,186,97,218,115,218,207,76,190,174,196,84,192,144]
result = []
flag = []
for i in range(0, len(msg), 2):
    result.append(DecryptCharacter(msg[i], msg[i+1]))

print("".join(i for i in result))

