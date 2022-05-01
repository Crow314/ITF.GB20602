if __name__ == '__main__':
    tmp = list(map(int, input().split()))
    P = tmp[0]
    T = tmp[1]

    heard = [set() for i in range(P)]

    while True:
        try:
            tmp = list(map(int, input().split()))
            heard[tmp[0]-1].add(tmp[1])
        except EOFError:
            break

    count = 0
    for i in range(P):
        for j in range(i+1, P):
            if i != j:
                if heard[i] != heard[j]:
                    count += 1

    if P == 1:
        count = 1
    print(count)
