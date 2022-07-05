import sys
import heapq

DIRECTIONS_EVEN = [[-1, -1], [0, -1], [-1, 0], [1, 0], [-1, 1], [0, 1]]  # i=0, 2, 4, ...
DIRECTIONS_ODD = [[0, -1], [1, -1], [-1, 0], [1, 0], [0, 1], [1, 1]]  # i=1, 3, 5, ...


def dfs(beehive: list, x: int, y: int) -> int:
    beehive[y][x] = '#'

    if y % 2 == 0:
        directions = DIRECTIONS_EVEN
    else:
        directions = DIRECTIONS_ODD

    child_depth = 0

    for direction in directions:
        child_x = x + direction[0]
        child_y = y + direction[1]

        if (child_x < 0) or (len(beehive[y]) <= child_x) or (child_y < 0) or (len(beehive) <= child_y):
            continue

        if beehive[child_y][child_x] == '#':
            continue

        child_depth += dfs(beehive, child_x, child_y)

    return child_depth + 1


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

            heapq.heappush(depths, dfs(beehive, x, y) * -1)  # desc

    honey = 0
    count = 0
    while honey < h:
        count += 1
        honey += heapq.heappop(depths) * -1  # desc

    print(count)


if __name__ == '__main__':
    main()
