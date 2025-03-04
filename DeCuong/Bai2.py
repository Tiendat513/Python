n=int(input("n"))
m=int(input("m"))
A=[]
for i in range(n):
    temp=[]
    for j in range(m):
        temp.append(int(input(f"[{i}][{j}]\n")))#In ra mhinh [i][j] với j lần lượt tăng, hết một vòng thì tăng i, tiếp tục tăng j cho đến khi hết i
    A.append(temp)
#In ra dong co tong lon nhat, nho nhat
max,min,pos1,pos2=-10**6,10**6,[],[] # tạo biến max, min với 10^6 để so sánh
for i in range(len(A)):
    temp=sum(A[i])
    if min>temp:    # so sánh để tìm min, max
        min,pos1=temp,A[i]  # gán giá trị min, max và vị trí
    if max<temp:
        max,pos2=temp,A[i]
print(f"day co tong max la:{pos2}")
print(f"day co tong min la:{pos1}")
#In ra tat ca cac so chia het cho 5
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j]%5==0:  #Ví dụ như A[0][0] % 5 == 0, Trong đó A[0][0] là tọa độ trong mảng 2 chiều
            print(A[i][j])

