def giaithua(x):
    S= 1
    for i in range(1,x+1):
        S*=i
    return S
print(giaithua(5))