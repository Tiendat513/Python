def pvung(A, dau, cuoi):
    moc = A[cuoi]
    i = dau - 1
    for j in range(dau, cuoi):
        if A[j] >= moc:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[cuoi] = A[cuoi], A[i + 1]
    return i + 1

def quickSort(A, dau, cuoi):
    if dau < cuoi:
        vitri = pvung(A, dau, cuoi)
        quickSort(A, dau, vitri - 1)
        quickSort(A, vitri + 1, cuoi)

# Example usage
A = [12, 4, 5, 6, 7, 3, 1, 105, 2, 8]
quickSort(A, 0, len(A) - 1)
print(A)
