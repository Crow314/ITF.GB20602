if __name__ == '__main__':
    N = int(input())

    while True:
        names = []

        for i in range(N):
            names.append(input())

        for i in range(N):
            for j in range(N-i-1):
                if names[j][:2] > names[j+1][:2]:
                    tmp = names[j]
                    names[j] = names[j+1]
                    names[j + 1] = tmp

        for name in names:
            print(name)

        N = int(input())

        if N == 0:
            break

        print()
