def chiahet(number):
    for i in range(len(str(number))):
        digits = int(str(number)[i]) 
        if digits!=0 and number%digits == 0:
            digits = digits+1
        else:
            return False
    return True
with open("SOCHIAHET.INP") as fi, open("SOCHIAHET.OUT", "w") as fo:
    n = int(fi.readline())
    A = list(map(int, fi.readline().split()))
    B=[]
    count=0
    for a in A:
        if chiahet(a):
            B.append(a)
            count+=1
    print(count,"\n", *B,file=fo)