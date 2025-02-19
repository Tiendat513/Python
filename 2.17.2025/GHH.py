def uoc(n):
    if n<=1:
        return False
    tong =1
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            tong+=i+n//1
    return 2*n<= tong, tong
print(uoc(16))