if __name__ == '__main__':
    N = int(input())

    minions = []
    for i in range(N):
        L, U = map(int, input().split())
        minions.append([L, U])

    minions.sort(reverse=True)

    counter = 0
    while minions:
        counter += 1
        L, U = minions.pop()
        while minions and ((L <= minions[-1][0] <= U) or (L <= minions[-1][1] <= U)):
            L2, U2 = minions.pop()
            L = max(L, L2)
            U = min(U, U2)

    print(counter)
