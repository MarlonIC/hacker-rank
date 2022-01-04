if __name__ == '__main__':
    n = int(input('Input number: '))

    output = ''
    for num in range(n):
        output += str(num + 1)

    print(output)
    print(*range(1, n + 1), sep='')
