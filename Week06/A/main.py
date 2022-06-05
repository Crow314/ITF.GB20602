import heapq


def adj_list(field: list, row: int, column:int) -> list:
    graph = [[] for _ in range(n*m)]

    directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]  # <v^>

    for i in range(row):
        for j in range(column):
            idx = i * column + j

            for direction in directions:
                x = j + field[i][j] * direction[0]
                y = i + field[i][j] * direction[1]

                next_idx = y * column + x

                if (x < 0) or (x >= m) or (y < 0) or (y >= n):
                    continue

                graph[idx].append(next_idx)

    return graph


def dijkstra(graph: list, start: int) -> list:
    count_list = [-1 for _ in range(len(graph))]
    count_list[start] = 0

    queue = []
    heapq.heappush(queue, start)

    while len(queue) > 0:
        node = heapq.heappop(queue)

        for next_node in graph[node]:
            next_count = count_list[node] + 1

            if (next_count < count_list[next_node]) or (count_list[next_node] == -1):
                count_list[next_node] = next_count
                heapq.heappush(queue, next_node)

    return count_list


if __name__ == '__main__':
    n, m = map(int, input().split())

    field = []

    for _ in range(n):
        num_list = [int(s) for s in list(input())]
        field.append(num_list)

    graph = adj_list(field, n, m)

    start = 0
    goal = m * n - 1

    counts = dijkstra(graph, 0)
    print(counts[goal])
