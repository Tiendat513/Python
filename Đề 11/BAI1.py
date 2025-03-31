with open("BAI1.INP", "r") as fi:
    n = int(fi.readline())
    count = 0         # Đếm số lượng số đã tìm được trong dãy A
    k = 1             # Số chia hiện tại (1, 2, 3, ...)
    current_num = 0   # Số tự nhiên đang xét, bắt đầu từ 0 để số 1 được xét đầu tiên
    result = 0        # Lưu kết quả là số thứ N
    while count < n:
        found_for_k = 0  # Đếm số lượng số chia hết cho k đã tìm được trong bước này
        while found_for_k < k:
            current_num += 1  # Xét số tự nhiên tiếp theo
            if current_num % k == 0:
                # Tìm thấy một số thỏa mãn chia hết cho k
                found_for_k += 1
                count += 1
                # Nếu đã tìm đủ N số, lưu lại và dừng
                if count == n:
                    result = current_num
                    break # Thoát vòng lặp tìm số cho k
        if count == n:
            break # Thoát vòng lặp chính khi đã đủ N số
        k += 1 # Chuyển sang số chia tiếp theo
print(result)