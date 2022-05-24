import math
from collections import deque


def hike(field: list, width: int, height: int, depth: int) -> bool:
    directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]  # <v^>
    search_queue = deque()
    visited = [[False for _ in range(width)] for _ in range(height)]

    for i in range(height):
        if field[i][0] <= depth:
            search_queue.append([0, i])  # [x, y]

    success = False

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

            if field[next_y][next_x] <= depth:
                if next_x == width-1:
                    success = True
                    break
                else:
                    search_queue.append([next_x, next_y])

        if success:
            break

    return success


if __name__ == '__main__':
    r, c = map(int, input().split())

    field = []

    for _ in range(r):
        field.append(list(map(int, input().split())))

    left = 0
    right = 1000000
    ans = -1

    while left < right:
        mid = math.ceil((left+right)/2)

        if hike(field, c, r, mid):
            ans = mid
            right = mid - 1
        else:
            left = mid

    print(ans)
