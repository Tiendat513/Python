def is_prime(n):
    """Kiểm tra xem số n có phải là số nguyên tố hay không."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Kiểm tra các ước số lẻ từ 3 đến sqrt(n)
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

# --- Hàm sinh các số đối xứng ---
def generate_palindromes(limit_N):
    palindromes = set()
    k = 1
    while True:
        s = str(k)
        s_rev = s[::-1]

        # Tạo số đối xứng lẻ
        palindrome_odd_str = s + s_rev[1:]
        palindrome_odd = int(palindrome_odd_str)

        if palindrome_odd > limit_N:
            break # Dừng khi số lẻ vượt quá giới hạn

        palindromes.add(palindrome_odd)

        # Tạo số đối xứng chẵn
        palindrome_even_str = s + s_rev
        palindrome_even = int(palindrome_even_str)

        if palindrome_even <= limit_N:
            palindromes.add(palindrome_even)

        k += 1

    return sorted(list(palindromes))

# --- Hàm giải quyết bài toán chính ---
with open("BAI1.INP", "r") as fi:
    line = fi.readline().split()
    if len(line) < 2:
        print("Loi: File input khong du 2 so M va N.")
        exit()
    M = int(line[0])
    N = int(line[1])
    # --- Xử lý ---
    # Bước 1: Sinh các số đối xứng nhỏ hơn hoặc bằng N
    candidate_palindromes = generate_palindromes(N)

    # Bước 2 & 3: Lọc theo M và kiểm tra nguyên tố
    result_primes = []
    for p in candidate_palindromes:
        if p >= M:
            # Nếu số đối xứng nằm trong khoảng [M, N], kiểm tra nguyên tố
            if is_prime(p):
                result_primes.append(p)
        # Không cần else vì generate_palindromes đã trả về list sắp xếp

    # --- Ghi Output ---
    with open("BAI1.OUT", "w") as fo:
        if not result_primes: # Nếu không tìm thấy số nào
            fo.write("0\n")
        else:
            for prime_palindrome in result_primes:
                fo.write(str(prime_palindrome) + "\n")