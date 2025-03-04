n=int(input("n"))
A=[]
for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(int(input(f"[{i}][{j}]")))
    #Dòng trên tương đương với...input("A["+str(i)+"]["+str(j)+"]")...
    A.append(temp)
#In ra tong duong cheo chinh, phu
sum1,sum2=0,0
for i in range(len(A)):
    sum1+= A[i] [i]         #Tính tổng đường chéo chính
    sum2+= A[i] [n-1-i] #]     #Tính tổng đường chéo phụ
print(f"Tổng đường chéo chính: {sum1}") 
print(f"Tổng đường chéo phụ: {sum2}")
    
    
    
"""
Vì ma trận có dạng NxN
Đường chéo chính là
[X][][]
[][X][]
[][][X]
Hay A[0][0], A[1][1], A[2][2],... A[n][n]
Đường chéo phụ là
[][][X]
[][X][]
[X][][]
Hay A[0][n], A[1][n-1], A[2][n-2],... A[n][0]
"""
