if __name__ == '__main__':
    N = int(input())
    QALY = 0.0

    for i in range(N):
        q, y = input().split()
        QALY += float(q) * float(y)

    print(QALY)
