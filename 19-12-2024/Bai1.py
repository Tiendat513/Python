N=10**9
def prime(b):
    if b <= 1:
        return False
    for i in range(2, int(b**0.5) + 1):
        if b % i == 0:
            return False
    return True
A=0
B=N
for i in range(N,0,-1):
    if prime(i):
        A=i
        break
while prime(B)==False:
    B+=1
    break
print(A,B)