def snt(x):
    if x==2 or x==3:
        return True
    if x>3:
        if x%2==0 or x%3==0:
            return False
        for i in range(5,int(x**0.5)+1,6):
            if x%i==0 or x%(i+2)==0:
                return False
        return True
print(snt(17))