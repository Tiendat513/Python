n=int(input("n"))
m=int(input("m"))
A=[]
for i in range(n):
    for j in range(m):
        temp=[]
        temp.append(int(input(f"[{i}][{j}]\n")))
    A.append(temp)

maxlor=0
minlor=0
pos1=[]
pos2=[]
for i in range(len(A)):
    temp=sum(A[i])
    if minlor>temp:
        minlor,pos1=temp,A[i]
        print(pos1)
    elif maxlor<temp:
        maxlor,pos2=temp,A[i]
print(f"day co tong max la:{pos2}")
print(f"day co tong min la:{pos1}")

