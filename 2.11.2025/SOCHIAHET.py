def checkuoc(s):
    for j in str(s):
        num=int(j)
        if num==0 or s%num!=0:
            return False
    else:
        return True
with open("SOCHIAHET.INP") as fo:
    s= int(fo.readline())
    A= list(map(int, fo.readline().split()))
B=[]
count=0
for i in range(s):
    if checkuoc(A[i]):
        B.append(A[i])
        count+=1
with open("SOCHIAHET.OUT", "w") as out:
    out.writelines(str(count)+"\n")
    for i in range(len(B)):
        out.writelines(str(B[i])+"\n")