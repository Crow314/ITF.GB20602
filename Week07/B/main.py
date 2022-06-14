from collections import deque

FAV = ['I', 'C', 'P', 'C', 'A', 'S', 'I', 'A', 'S', 'G']
DIRECTIONS = [
    [-2, -1], [-1, -2],  # Up-Left
    [2, -1], [1, -2],  # Up-Right
    [-2, 1], [-1, 2],  # Down-Left
    [2, 1], [1, 2]  # Down-Right
]


def bfs(N: int, field: list, start: list) -> bool:
    queue = deque(start)

    while len(queue) > 0:
        cell = queue.popleft()

        for direction in DIRECTIONS:
            x = cell[0] + direction[0]
            y = cell[1] + direction[1]
            next_idx = cell[2] + 1

            if (x < 0) or (x >= N) or (y < 0) or (y >= N):
                continue

            if field[y][x] == FAV[next_idx]:
                if next_idx == 9:  # len(FAV)-1
                    return True

                queue.append([x, y, next_idx])

    return False


def main():
    N = int(input())
    S = list(input())

    field = [[None for _ in range(N)] for _ in range(N)]
    start_cells = []

    idx = 0
    for i in range(N):
        for j in range(N):
            c = S[idx]
            field[i][j] = c
            idx += 1

            if c == FAV[0]:
                start_cells.append([j, i, 0])  # [x, y, fav_idx]

    res = 'YES' if bfs(N, field, start_cells) else 'NO'
    print(res)


if __name__ == '__main__':
    main()
