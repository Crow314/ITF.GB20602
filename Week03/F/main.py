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

    for obstacle in obstacles:
        if obstacle[1] == level:
            count += 1
        else:
            break

    print(str(level) + ' ' + str(count))
