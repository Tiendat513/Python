def check(n):
    orgin=n
    sum=0
    while n>0:
        digit= n%10
        sum+= digit**3
        n//=10
    return sum==orgin

with open("SOTUMAN.INP") as fi, open("SOTUMAN.OUT","w") as fo:
    n= int(fi.readline())
    A= list(map(int, fi.readline().split()))
    List=[]
    for i in(A):
        if check(i):
            List.append(i)
    if len(List)==0:
        fo.write("-1")
    else:
        List.sort()
    print(*List,file=fo)
