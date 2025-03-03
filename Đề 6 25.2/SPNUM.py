def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def count(A, B):
    count = 0
    for i in range(2, int(B**0.5) + 1):
        if isPrime(i):
            special_number = i * i
            if A <= special_number <= B:
                count += 1
    return count
with open('SPNUM.INP') as fi, open('SPNUM.OUT', 'w') as fo:
    line= list(map(int,fi.readline().split()))
    start= line[0]
    
    end= line[1]
    count= count(start, end)
    fo.write(str(count))
print(count)