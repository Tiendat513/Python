with open("CTREE.INP") as fi, open ("CTREE.OUT","w") as fo:
    n= int(fi.readline())
    A=list(map(int,(fi.readline().split())))
    A.sort()
    min = A[0]
    count=0
    for i in range(n):
        if A[i]== min:
            count+=1
        else:
            break
    print(f"{count} {n-count}", file=fo)