import sys
sys.stdin=open('BAI2.INP')
from collections import Counter
A=input()
B=sorted(A)
print(Counter(B))