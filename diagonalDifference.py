def diagonal_difference(arr):
    primary_diagonal = 0
    secondary_diagonal = 0
    for index in range(len(arr)):
        primary_diagonal += arr[index][index]
        secondary_diagonal += arr[index][-(index+1)]
    return abs(primary_diagonal - secondary_diagonal)


arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]
print(diagonal_difference(arr))
