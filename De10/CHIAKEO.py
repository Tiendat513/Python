def chia_keo(a):
    n = len(a)
    total_sum = sum(a)
    half_sum = total_sum // 2
    dp = [False] * (half_sum + 1)
    dp[0] = True

    for num in a:
        for i in range(half_sum, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    result = 0
    for i in range(half_sum, -1, -1):
        if dp[i]:
            result = i
            break

    diff = total_sum - 2 * result
    
    # Tìm các gói kẹo thuộc phần thứ nhất
    subset = []
    current_sum = result
    for i in range(n - 1, -1, -1):
        if a[i] <= current_sum and dp[current_sum - a[i]]:
            subset.append(i + 1)
            current_sum -= a[i]
            
    subset.sort()

    return diff, subset
with open("CHIAKEO.INP") as fi, open("CHIAKEO.OUT","w") as fo:
    n=int(fi.readline())
    a=list(map(int,fi.readline().split()))
    diff, subset=chia_keo(a)
    fo.write(f"{diff}\n{subset}")