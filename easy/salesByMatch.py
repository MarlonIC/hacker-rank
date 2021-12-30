def sock_merchant(n, ar):
    total_pairs = 0
    pairs = 2
    matrix = {}
    for index in range(n):
        if ar[index] not in matrix:
            matrix[ar[index]] = [ar[index]]
        else:
            matrix[ar[index]].append(ar[index])

    for value in matrix.values():
        total_pairs += len(value) // pairs

    return total_pairs


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sock_merchant(n, ar))
