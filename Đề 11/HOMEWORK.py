with open("HOMEWORK.INP", "r") as fi:
    N,Skill= map(int,fi.readline().split())
    A= list(map(int,fi.readline().split()))
    A.sort()
    count = 0
    for i in A:
        if Skill>=i:
            Skill+=i
            count+=1
        else:
            break
with open("HOMEWORK.OUT", "w") as fo:
    fo.write(str(count))