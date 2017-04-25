UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"
NUM   = "1234567890"
SYM   = "~!@#$%^&*()`"
BLACK = ''''"\n '''

upper = 0
lower = 0
num   = 0
sym   = 0
valid = 0

def difftype(c1, c2):
    if c1 in UPPER and c2 in UPPER:
        return False
    if c1 in LOWER and c2 in LOWER:
        return False
    if c1 in NUM and c2 in NUM:
        return False
    if c1 in SYM and c2 in SYM:
        return False
    return True

def calcrank(pw): 
    rank = 5
    plen = len(pw)
    
    if plen < 8: 
        rank -= 1
    if plen > 11:
        rank += 1
    if plen > 15:
        rank += 1
    syms = [ c in SYM for c in pw ]
    for c in syms:
        if c:
            rank += 1
            break

    chains = len([ (c1, c2) for c1, c2 in zip(pw, pw[1:]) if difftype(c1, c2) ])
    if chains < plen / 8:
        rank -= 1
    if chains < plen / 5:
        rank -= 1
    if chains > plen / 4:
        rank += 1
    if chains > plen / 3:
        rank += 1

    nums = len([c for c in pw if c in NUM])
    if nums < 3:
        rank -= 1

    return rank

# Input Loop
while True:
    valid = 0
    raw   = raw_input("Please enter a password: ")
    chars = [i for i in raw]
    plen  = len(chars)
    
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
        print "Your password is weak."
    else:
        print "Your password has potential. I'd give it a", calcrank(chars), "out of 10."
    print "\nWhy not try another password?"
