if __name__ == '__main__':
    N = int(input())
    lista = []

    for _ in range(N):
        command = input()
        command = command.split(' ')
        if command[0].lower() == 'insert':
            lista.insert(int(command[1]), int(command[2]))
        elif command[0].lower() == 'print':
            print(lista)
        elif command[0].lower() == 'remove':
            lista.remove(int(command[1]))
        elif command[0].lower() == 'append':
            lista.append(int(command[1]))
        elif command[0].lower() == 'sort':
            lista.sort()
        elif command[0].lower() == 'pop':
            lista.pop()
        elif command[0].lower() == 'reverse':
            lista.reverse()

