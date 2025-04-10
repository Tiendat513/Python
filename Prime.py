import sys
import re
# Cần cài đặt thư viện sympy: pip install sympy
try:
    from sympy import isprime
except ImportError:
    print("Lỗi: Thư viện sympy chưa được cài đặt.")
    print("Hãy chạy: pip install sympy")
    sys.exit(1)

def solve_with_sympy():
    T = sys.stdin.readline().strip()
    n = len(T)

    digit_count = 0
    largest_prime = 0
    numbers_to_check = set() # Dùng set để tránh kiểm tra trùng lặp

    # 1. Đếm chữ số và trích xuất các khối số
    current_block = ""
    for i in range(n):
        char = T[i]
        if '0' <= char <= '9':
            digit_count += 1
            current_block += char
        else:
            # Nếu gặp ký tự không phải số và có block số đang xây dựng
            if current_block:
                # Xử lý tất cả các chuỗi con của block này
                len_block = len(current_block)
                for j in range(len_block):
                    for k in range(j, len_block):
                        sub = current_block[j : k+1]
                        # Kiểm tra leading zero (trừ khi là số 0)
                        if len(sub) > 1 and sub[0] == '0':
                            continue
                        try:
                            p_val = int(sub)
                            numbers_to_check.add(p_val)
                        except ValueError:
                            continue # Bỏ qua nếu không phải số hợp lệ
                current_block = "" # Reset block

    # Xử lý block cuối cùng nếu có
    if current_block:
        len_block = len(current_block)
        for j in range(len_block):
            for k in range(j, len_block):
                sub = current_block[j : k+1]
                if len(sub) > 1 and sub[0] == '0':
                    continue
                try:
                    p_val = int(sub)
                    numbers_to_check.add(p_val)
                except ValueError:
                    continue

    # 2. Kiểm tra nguyên tố các số đã thu thập
    for p in numbers_to_check:
        # Sử dụng hàm isprime mạnh mẽ của sympy
        if isprime(p):
            largest_prime = max(largest_prime, p)

    # 3. In kết quả
    print(digit_count)
    print(largest_prime)

# --- Chạy chương trình ---
solve_with_sympy()