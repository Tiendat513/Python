import sys
from collections import defaultdict

def solve():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    remainder_counts = defaultdict(int)
    # Khởi tạo cho tiền tố tổng ban đầu P[0] = 0
    remainder_counts[0] = 1

    total_count = 0
    current_sum = 0

    for x in a:
        current_sum += x
        remainder = current_sum % k

        # Cộng số lượng tiền tố trước đó có cùng remainder
        total_count += remainder_counts[remainder]

        # Tăng count cho remainder hiện tại
        remainder_counts[remainder] += 1

    print(total_count)

solve()