import sys
sys.stdin = open('STEP.INP', 'r')
sys.stdout = open('STEP.OUT', 'w')
n=int(input())
A=list(map(int, input().split()))
def check(n):
    s=str(n)
    if len(s)==1:
        return False
    for i in range(len(s)-1):
        if s[i]>s[i+1]:
            return False
    return True
count=0
for i in range(n):
    if check(A[i]):
       count+=1
print(count)
# Đếm số lượng số nguyên dương có chữ số tăng dần trong mảng A