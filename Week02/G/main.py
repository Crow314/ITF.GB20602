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

    opinions = []
    for i in range(P):
        flg = True
        for j in range(len(opinions)):
            if heard[i] == opinions[j]:
                flg = False
        if flg:
            opinions.append(heard[i])

    print(len(opinions))
