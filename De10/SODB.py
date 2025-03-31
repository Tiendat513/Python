def songuyento(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def chanle(n):
    for i in range(len(str(n))):
        countchan=0
        countle=0
        if str(n)==1:
            return False
        if int(str(n)[i])%2==0:
            countchan+=1
        else:
            countle+=1
    if countchan==countle:
        return False
    else: return True
with open('SODB.INP', 'r') as fi, open('SODB.OUT', 'w') as fo:
    m=int(fi.readline())
    A= list(map(int,fi.readline().split()))
    count=0
    for i in range(m-1):
        now=A[i]
        if songuyento(now)==True and chanle(now)==True:
            count+=1
    fo.write(str(count))