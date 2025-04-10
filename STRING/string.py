import sys
sys.stdin=open("BAI3.INP","r")
sys.stdout=open("BAI3.OUT","w")
A=list(input().split())
C=""
count=0
for i in A:
    for j in (i):
        C+=j.upper()
        count+=1
    C+=" "
print(C)
print(count+len(A)-1)