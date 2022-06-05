import heapq

MAX_VALUE = 10 ** 9


def adj_list(h: int, w: int) -> list:
    graph = [[] for _ in range(h * w)]

    directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]

    for i in range(h):
        for j in range(w):
            idx = i * w + j

            for direction in directions:
                x = j + direction[0]
                y = i + direction[1]

                if (x < 0) or (x >= w) or (y < 0) or (y >= h):
                    continue
                next_idx = y * w + x

                graph[idx].append(next_idx)

    return graph


def dijkstra(graph: list, costs: list, start_nodes: list) -> list:
    paths = [[MAX_VALUE, MAX_VALUE] for _ in range(len(graph))]  # [src, cost]
    queue = []

    for start_node in start_nodes:
        paths[start_node][1] = costs[start_node]
        heapq.heappush(queue, start_node)

    while len(queue) > 0:
        node = heapq.heappop(queue)

        for next_node in graph[node]:
            next_cost = paths[node][1] + costs[next_node]

            if next_cost < paths[next_node][1]:
                paths[next_node][0] = node
                paths[next_node][1] = next_cost
                heapq.heappush(queue, next_node)

    return paths


def main():
    h, w = map(int, input().split())
    while True:
        strengths = []

        for _ in range(h):
            num_list = [int(s) for s in list(input())]
            strengths += num_list

        graph = adj_list(h, w)
        start_nodes = [i for i in range(w)]

        paths = dijkstra(graph, strengths, start_nodes)

        goal_node = MAX_VALUE
        goal_cost = MAX_VALUE
        for i in range(w*(h-1), h*w):
            cost = paths[i][1]
            if cost < goal_cost:
                goal_node = i
                goal_cost = cost

        path = goal_node
        result_paths = []
        while True:
            result_paths.append(path)
            path = paths[path][0]
            if path == MAX_VALUE:
                break

        for i in range(h):
            for j in range(w):
                idx = i * w + j
                if idx in result_paths:
                    print(' ', end='')
                else:
                    print(strengths[idx], end='')
            print()

        # next block
        h, w = map(int, input().split())

        if (h == 0) and (w == 0):
            break

        print()


if __name__ == '__main__':
    main()
