import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    # Bước 1: Sắp xếp danh sách năng lực
    a.sort()

    max_diff = 0
    # Bước 2: Ghép cặp liền kề và tính chênh lệch
    # Ghép (a[0], a[1]), (a[2], a[3]), ..., (a[2N-2], a[2N-1])
    for i in range(0, 2 * n, 2):
        diff = a[i+1] - a[i]
        if diff > max_diff:
            max_diff = diff

    # In ra kết quả
    print(max_diff)

# Gọi hàm giải
solve()