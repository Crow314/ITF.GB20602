import sys

directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]  # <v^>
gold_count = 0


def dfs(field: list, visited: list, w: int, h: int):
    global gold_count
    visited[h][w] = True

    if field[h][w] == 'G':
        gold_count += 1

    for direction in directions:
        next_w = w + direction[0]
        next_h = h + direction[1]

        if field[next_h][next_w] == 'T':
            return

    for direction in directions:
        next_w = w + direction[0]
        next_h = h + direction[1]

        if (next_w < 0) or (next_w >= W) or (next_h < 0) or (next_h >= H):
            continue

        if field[next_h][next_w] == '#':
            continue

        if visited[next_h][next_w]:
            continue

        dfs(field, visited, next_w, next_h)


if __name__ == '__main__':

    W, H = map(int, input().split())
    field = []

    for _ in range(H):
        field.append(list(input()))

    player = [-1, -1]
    for i in range(H):
        try:
            tmp_pos = field[i].index('P')
            player = [i, tmp_pos]
        except ValueError:
            pass

    visited = [[False for _ in range(W)] for _ in range(H)]

    sys.setrecursionlimit(10 ** 5)
    dfs(field, visited, player[1], player[0])

    print(gold_count)
