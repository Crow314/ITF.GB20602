if __name__ == '__main__':
    N, H = list(map(int, input().split()))

    obstacles = [[i, 0] for i in range(H)]

    for i in range(N):
        height = int(input())
        if i % 2 == 0:
            obstacles[0][1] += 1
            obstacles[height-1][1] += -1
        else:
            obstacles[H-height-1][1] += 1

    for i in range(1, H):
        obstacles[i][1] += obstacles[i-1][1]

    obstacles.sort(key=lambda x: x[1])

    level = obstacles[0][1]
    count = 0

    for obstacle in obstacles:
        if obstacle[1] == level:
            count += 1
        else:
            break

    print(str(level) + ' ' + str(count))
