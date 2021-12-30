def counting_valleys(steps, path):
    sea_level = 0
    steps_arr = [sea_level]
    valleys = []
    valley = []

    for index in range(steps):
        if path[index] == 'U':
            sea_level += 1
        elif path[index] == 'D':
            sea_level -= 1

        if sea_level == 0:
            steps_arr.append(0)

        steps_arr.append(sea_level)

    for value in steps_arr:
        valley.append(value)
        if valley[-1] == 0 and len(valley) != 1:
            if valley[0] == 0 and valley[1] == -1 and valley[-1] == 0 and valley[-2] == -1:
                valleys.append(valley)
            valley = []

    return len(valleys)


steps = 12
path = 'DDUUDDUDUUUD'
print(counting_valleys(steps, path))
# matrix = {}
# matrix[len(matrix)] = [0, 1, 0]
# print(matrix)
# print(len(matrix))
