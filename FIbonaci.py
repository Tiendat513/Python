def fibonacy(n):
    s1=0
    s2=1
    S=s1+s2
    for i in range(1,n-1):
        s1,s2=s2,S
        S+=s2+s1
    return s2
print(fibonacy(7))