import sys
sys.stdin=open('GIFTS.INP')
sys.stdout=open('GIFTS.OUT','w')
n=int(input())
items = []
totalb = 0
for _ in range(n):
    a, b = map(int, input().split())
    items.append((a - b, a, b))
    totalb += b

items.sort(reverse=True)

max_total_value = totalb
for i in range(n // 2):
    max_total_value += items[i][0] 

print(max_total_value)