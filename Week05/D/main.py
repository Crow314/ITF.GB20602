from collections import deque

if __name__ == '__main__':
    N, M = map(int, input().split())

    width = M + 2
    height = N + 2

    island = [[] for _ in range(height)]
    visited = [[False for _ in range(width)] for _ in range(height)]

    island[0] = [False for _ in range(width)]  # North Blue

    for i in range(N):
        island[i+1].append(False)  # West Blue
        for v in list(input()):
            if v == '0':
                island[i+1].append(False)
            elif v == '1':
                island[i+1].append(True)
            else:
                raise Exception
        island[i+1].append(False)  # East Blue

    island[N+1] = [False for _ in range(width)]  # South Blue

    search_queue = deque()
    search_queue.append([0, 0])  # [x, y]

    directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]  # <v^>

    count = 0

    while len(search_queue) > 0:
        pos = search_queue.popleft()
        x = pos[0]
        y = pos[1]

        if visited[y][x]:
            continue

        visited[y][x] = True

        for direction in directions:
            next_x = x + direction[0]
            next_y = y + direction[1]

            if (next_x < 0) or (next_x >= width) or (next_y < 0) or (next_y >= height):  # Out of range
                continue

            if visited[next_y][next_x]:
                continue

            if island[next_y][next_x]:
                count += 1
            else:  # ocean
                search_queue.append([next_x, next_y])
            pass

    print(count)
