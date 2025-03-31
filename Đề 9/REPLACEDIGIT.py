with open("REPLACEDIGIT.INP") as fi, open("REPLACEDIGIT.OUT", "w") as fo:
    m=int(fi.readline())
    for i in range(m):
        fo.write(fi.readline().replace("0", "5"))