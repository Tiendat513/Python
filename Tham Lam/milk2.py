import sys
sys.stdin=open("Milk2.INP","r")
sys.stdout=open("Milk2.OUT","w")
n=int(input())
A=list(map(int, input().split()))
A.sort(reverse=True)
Mil=0
for i in range(len(A)):
    if A[i]-i>=0:
        Mil= Mil+(A[i]-i)
    else: break
print(Mil)
