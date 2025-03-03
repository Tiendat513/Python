def solve(i):
    global current
    for j in range(i):
        if current+1%i!=0:
            current+=1
        else:
            current+=i
            A.append(current)
        
with open("BL2.INP", "r") as f:
    k = int(f.readline())
    current = 0
    A = []
    i = 0
    while len(A)<k:
        i+=1
        solve(i)
    print(A)