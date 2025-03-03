with open("BL1.INP") as fi, open("BL1.OUT","w") as fo:
    x,y= fi.read().split()
    res=0
    for i in range(len(x)):
        res+=(min(abs(int(x[i])-int(y[i])),10-abs(int(x[i])-int(y[i]))))
    print(res, file = fo)
        