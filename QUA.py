import sys

# --- Fenwick Tree (BIT) cho Max - Iterative ---
# bit_tree và num_unique_labels sẽ được định nghĩa trong hàm solve
bit_tree = []
num_unique_labels = 0

def update_bit(idx, value):
    # Cập nhật giá trị lớn nhất tại idx và các nút cha
    # idx là chỉ số nén (0-based), chuyển sang 1-based cho BIT
    idx += 1
    while idx <= num_unique_labels:
        bit_tree[idx] = max(bit_tree[idx], value)
        idx += idx & (-idx) # Đi đến nút cha tiếp theo

def query_bit(idx):
    # Truy vấn giá trị lớn nhất trong khoảng [0, idx] (chỉ số nén)
    # idx là chỉ số nén (0-based), chuyển sang 1-based cho BIT
    idx += 1
    max_val = 0
    while idx > 0:
        max_val = max(max_val, bit_tree[idx])
        idx -= idx & (-idx) # Đi đến nút tổ tiên quản lý tiền tố
    return max_val
# --- Kết thúc phần BIT ---

def solve():
    global bit_tree, num_unique_labels
    n = int(sys.stdin.readline())
    if n == 0:
        sys.stdout.write("0\n")
        return

    # 1. Đọc và chuẩn bị dữ liệu
    boxes = []
    labels = set()
    for _ in range(n):
        a, w = map(int, sys.stdin.readline().split())
        boxes.append((a, w)) # Lưu dạng tuple (nhãn, giá trị)
        labels.add(a)

    # 2. Coordinate Compression
    sorted_unique_labels = sorted(list(labels))
    label_to_compressed_idx = {label: idx for idx, label in enumerate(sorted_unique_labels)}
    num_unique_labels = len(sorted_unique_labels)

    # 3. Sắp xếp hộp quà theo nhãn
    boxes.sort()

    # 4. Khởi tạo BIT
    bit_tree = [0] * (num_unique_labels + 1)

    # 5. Tính toán DP và cập nhật BIT
    for a, w in boxes:
        compressed_idx = label_to_compressed_idx[a]

        # Tìm max DP của các nhãn nhỏ hơn nhãn hiện tại
        max_prev_dp = query_bit(compressed_idx - 1)

        # Tính DP cho nhãn hiện tại
        current_dp = w + max_prev_dp

        # Cập nhật BIT với giá trị DP mới này tại chỉ số nén tương ứng
        update_bit(compressed_idx, current_dp)

    # 6. Kết quả là max của toàn bộ cây BIT
    final_max_value = query_bit(num_unique_labels - 1)

    sys.stdout.write(str(final_max_value) + '\n')

# --- Chạy chương trình ---
solve()