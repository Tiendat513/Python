import sys
import math
sys.stdin = open('UCLN.inp', 'r')
sys.stdout = open('UCLN.out', 'w')
a,b=map(int,input().split())
print(f"{math.gcd(a,b)}")