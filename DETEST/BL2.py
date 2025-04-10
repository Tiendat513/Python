import sys
sys.stdin = open('BL2.INP', 'r')
sys.stdout = open('BL2.OUT', 'w')
n=int(input())
A=list(map(int, input().split()))
A.sort()
haidau1duoi=A[0]*A[1]*A[len(A)-1]
baduoi=A[len(A)-1]*A[len(A)-2]*A[len(A)-3]
print(max(haidau1duoi,baduoi))