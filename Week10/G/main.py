import math

MAX_VALUE = 10 ** 12


def calc_dist(pos: list, i: int, j: int) -> float:
    return math.sqrt((pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2)


def create_adj_matrix(pos: list, n: int) -> list:
    adj_matrix = [[MAX_VALUE for _ in range(n)] for _ in range(n)]

    for i in range(n):
        adj_matrix[i][i] = 0
        adj_matrix[0][i] = calc_dist(pos, 0, i) / 5

    for i in range(1, n-1):
        for j in range(1, n):
            if i == j:
                continue

            dist = calc_dist(pos, i, j)
            adj_matrix[i][j] = min((abs(dist - 50) / 5) + 2, dist / 5)

    return adj_matrix


def floyd_warshall(graph: list):
    V = len(graph)

    for k in range(V):
        for src in range(V):
            for dst in range(V):
                graph[src][dst] = min(graph[src][dst], graph[src][k] + graph[k][dst])


def main():
    src = list(map(float, input().split()))  # [X, Y]
    dst = list(map(float, input().split()))

    n = int(input())

    pos = []  # [0:n+2]

    pos.append(src)  # [0]
    for _ in range(n):
        pos.append(list(map(float, input().split())))
    pos.append(dst)  # [n+1]

    adj_matrix = create_adj_matrix(pos, n+2)
    floyd_warshall(adj_matrix)

    print(adj_matrix[0][n+1])


if __name__ == '__main__':
    main()
