import sys
sys.stdin=open("tile.INP","r")
sys.stdout=open("tile.OUT","w")
n=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
max_height = 0
for k in range(n):
    can_add = True
    for j in range(k):
        bricks_above = k - j
        if A[j] < bricks_above:
            can_add = False
            break            
    if can_add:
        max_height = k + 1
    else:
        break 
print(max_height)
