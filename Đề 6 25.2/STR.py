with open("STR.INP") as fi, open ("STR.OUT","w") as fo:
    A= fi.readline()
    error=0
    for i in range(len(A)):
        if A[i] not in"01":
            error+=1
    fo.write(str(error))