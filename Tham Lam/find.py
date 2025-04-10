import sys
sys.stdin=  open("find.INP")
sys.stdout=open("find.OUT","w")
m = int(sys.stdin.readline())

if m == 0:
    print(10)
elif m == 1:
    print(1)
else:
    digits = []
    for d in range(9, 1, -1):
        while m % d == 0:
            digits.append(d)
            m = m // d 

    if m > 1:
        print("-1")
    else:
        digits.reverse()
        print("".join(map(str, digits)))
