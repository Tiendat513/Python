with open("THREENUM.INP") as f, open("THREENUM.OUT", "w") as fo:
    n= int(f.readline().strip())
    A=list(map(int, f.readline().split()))
    max_left = [0]*n
    max_right = [0]*n
    max_left[0] = A[0]
    max_right[n-1] = A[n-1]
    for i in range(1, n):
        max_left[i]=max(max_left[i-1], A[i])
    for i in range(n-2, -1, -1):
        max_right[i]=max(max_right[i+1], A[i])
    res = 0
    for i in range(n):
        res = max(res, 2*max_left[i]-3*A[i]+5*max_right[i]-A[i])
    print(res,file=fo)