import bisect

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        m = int(input())
        tmp = list(map(int, input().split()))

        dolls = [[0, 0] for _ in range(m)]

        for i in range(0, m):
            dolls[i][0] = tmp[i*2]
            dolls[i][1] = -tmp[i*2 + 1]

        dolls = sorted(dolls, key=lambda x: (x[0], x[1]))
        seq = []

        for doll in dolls:
            seq.append(doll[1])

        LDS = [seq[0]]
        for i in range(1, len(seq)):
            idx = bisect.bisect_right(LDS, seq[i])
            if idx >= len(LDS):
                LDS.append(seq[i])
            else:
                LDS[idx] = seq[i]

        print(len(LDS))
