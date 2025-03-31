#Tìm số nguyên tố 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
with open('BAI1.INP', 'r') as fo, open('BAI1.OUT', 'w') as fi:
    n = int(fo.readline())
    for i in range(n):
        a = int(fo.readline())
        if is_prime(a):
            fi.write(str(1) + '\n')
        else:
            fi.write(str(0) + '\n')
    