if __name__ == '__main__':
    N = int(input())
    baloons_n = list(map(int, input().split()))

    h_n = max(baloons_n)
    count = 0

    while len(baloons_n) > 0:
        baloons_c = baloons_n
        baloons_n = list()

        h_c = h_n
        h_n = 0

        count += 1

        for v in baloons_c:
            if v == h_c:
                h_c -= 1
            else:
                if v > h_n:
                    h_n = v
                baloons_n.append(v)

    print(count)
