A=[1,1,2,2,11,3,10,10,10,10]
'''Tien xu ly prefix'''
B=[0]
current=0
def DCKG(a,b):
    return B[b-1]-B[a-1]==0
for i in range(1,len(A)):
    if A[i]>=A[i-1]:
        B.append(current)
    else:
        current+=1
        B.append(current)

print(B)