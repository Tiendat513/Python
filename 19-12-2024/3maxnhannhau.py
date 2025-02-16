with open("INPUT.INP") as f:
        A = list(map(int, f.read().split()))
B=1
C=list(set(A))      
C.sort
for i in range(1,4):
    B= B*C[len(C)-i]
    
with open("OUTPUT.OUT","w" ) as f2:
    f2.write(str(B))
    