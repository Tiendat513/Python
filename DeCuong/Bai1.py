# Nhap vao so nguyen N, sau do nhap N phan tu vao mang A
N= int(input("Nhap so nguyen N"))
A=[]
for i in range(N):
    A.append(int(input("Nhap phan tu thu "+str(i+1))))
#Tim so lon nhat
max=A[0]
for i in range(1,N):
    if A[i]>max:
        max=A[i]
#Tim vi tri cua so lon nhat
for i in range(N):   
    if A[i]==max:
        print(i+1)
#dem trong N so co bao nhieu so chia het cho 5
count=0
for i in range(N):
    if A[i]%5==0:
        count+=1
print(count)
#Tinh tong binh phuong cac so le
sum=0
for i in range(N):
    if A[i]%2!=0:
        sum+=A[i]**2
print(sum)
#Tim va in ra so 5 xuat hien dau tien, cuoi cung
first=-1
last=-1
for i in range(N):
    if A[i]==5:
        first=i+1
        break
for i in range(N-1,first-2,-1):
    if A[i]==5:
        last=i+1
        break
print(first)
print(last)
#Sap xep chen
for i in range(1,N):
    key=A[i]
    j=i-1
    while j>=0 and key<A[j]:
        A[j+1]=A[j]
        j-=1
    A[j+1]=key
print(A)
#Sap xep chon
for i in range(N):
    min=i
    for j in range(i+1,N):
        if A[j]<A[min]:
            min=j
    A[i],A[min]=A[min],A[i]
print(A)
#Sap xep noi bot
for i in range(N):
    for j in range(0,N-i-1):
        if A[j]>A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]
print(A)
