import math
with open("DAYUCLN.INP", "r") as f, open("DAYUCLN.OUT", "w") as fo: 
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    def solve(n,a):
        b = [0] * (n + 1)
        for i in range(n - 1):
            b[i + 1] = lcm(a[i], a[i + 1])
        b[0] = a[0]
        b[n] = a[n - 1]
        print(*b,file=fo)
    t=int(f.readline())
    for _ in range(t):
        n = int(f.readline())
        a = list(map(int, f.readline().split()))
        solve(n,a)