if __name__ == '__main__':
    N, H = list(map(int, input().split()))

    obstacles = [[i, 0] for i in range(H)]

    for i in range(N):
        height = int(input())
        if i % 2 == 0:
            for j in range(0, height):
                obstacles[j][1] += 1
        else:
            for j in range(H - height, H):
                obstacles[j][1] += 1

    obstacles.sort(key=lambda x: x[1])

    level = obstacles[0][1]
    count = 0
    idx = 0

    # bisection search
    left = 0
    right = H - 1
    while True:
        if right - left <= 1:
            break

        idx = int((left + right) / 2)

        if obstacles[idx][1] == level:
            left = idx
            continue
        if obstacles[idx][1] > level:
            right = idx
            continue

    for i in range(idx-1, N):
        if obstacles[i][1] != level:
            count = i
            break

    print(str(level) + ' ' + str(count))
