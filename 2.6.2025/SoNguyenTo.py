def prime(b):
    if b <= 1:
        return False
    for i in range(2, int(b**0.5) + 1):
        if b % i == 0:
            return False
    return True
f = open("BAI1.INP")
sl= int(f.readline())
with open ("BAI1.OUT","w") as fo:
    for i in range(sl):
        n= int(f.readline())
        if prime(n):
            fo.writelines("1\n")
        else:
            fo.writelines("0\n")
