raw = raw_input("Please enter a password: ")
chars = [i for i in raw]

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"
NUM   = "1234567890"
SYM   = "~!@#$%^&*()`"
BLACK = ''''"\n '''

plen  = len(chars)
upper = 0
lower = 0
num   = 0
sym   = 0
valid = 0

for c in chars:
    if c in UPPER:
        upper += 1
    elif c in LOWER:
        lower += 1
    elif c in NUM:
        num += 1
    elif c in SYM:
        sym += 1
    else:
        valid = -1
        break
    
if valid < 0 or plen < 6 or upper < 2 or lower < 2 or num < 1:
    print "Your password is garbage."
else:
    print "Your password has potential."
