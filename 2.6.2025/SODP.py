def prime(b):
    if b <= 1:
        return False
    for i in range(2, int(b**0.5) + 1):
        if b % i == 0:
            return False
    return True
with open("SODP.INP") as f:
    n= f.readline()
    S =list(map(int, f.readline().split()))
A=0
for i in range(len(S)):
    if len(str(S[i]))>2:
           chan=0
           le=0
           for j in range(len(str(S[i]))):
               if S[j]%2==0:
                   chan+=1
               else:
                le+=1
           if chan!=le and prime(S[i]):
                   A+=1
with open("SODP.OUT","w") as fo:
    fo.write(str(A))