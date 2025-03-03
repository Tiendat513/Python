def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes
def count(A, B):
    limit = int(B**0.5) + 1  
    primes = sieve(limit)
    count = 0
    for i in range(2, limit):
        if primes[i]:
            special_number = i * i
            if A <= special_number <= B:
                count += 1
    return count
with open('SPNUM.INP', 'r') as fi, open('SPNUM.OUT', 'w') as fo:
    A, B = map(int, fi.readline().split())
    result = count(A, B)
    fo.write(str(result))