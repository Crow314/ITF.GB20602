import sys
import heapq
from collections import deque

DIRECTIONS_EVEN = [[-1, -1], [0, -1], [-1, 0], [1, 0], [-1, 1], [0, 1]]  # i=0, 2, 4, ...
DIRECTIONS_ODD = [[0, -1], [1, -1], [-1, 0], [1, 0], [0, 1], [1, 1]]  # i=1, 3, 5, ...


def bfs(beehive: list, start_x: int, start_y: int) -> int:
    queue = deque()
    area_size = 0

    queue.append([start_x, start_y])

    while len(queue):
        x, y = queue.popleft()

        if beehive[y][x] == '#':
            continue

        area_size += 1
        beehive[y][x] = '#'

        if y % 2 == 0:
            directions = DIRECTIONS_EVEN
        else:
            directions = DIRECTIONS_ODD

        for direction in directions:
            child_x = x + direction[0]
            child_y = y + direction[1]

            if (child_x < 0) or (len(beehive[y]) <= child_x) or (child_y < 0) or (len(beehive) <= child_y):
                continue

            if beehive[child_y][child_x] == '#':
                continue

            queue.append([child_x, child_y])

    return area_size


def main():
    h, n, m = map(int, input().split())

    beehive = []
    for _ in range(n):
        beehive.append(input().split())

    depths = []

    sys.setrecursionlimit(10 ** 6)

    for y in range(n):
        for x in range(m):
            if beehive[y][x] == '#':
                continue

            heapq.heappush(depths, bfs(beehive, x, y) * -1)  # desc

    honey = 0
    count = 0
    while honey < h:
        count += 1
        honey += heapq.heappop(depths) * -1  # desc

    print(count)


if __name__ == '__main__':
    main()
