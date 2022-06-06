from collections import deque
import heapq

MAX_VALUE = 10 ** 9


def dijkstra(graph: list) -> list:
    vertex_count = len(graph)
    paths = [[MAX_VALUE, set()] for _ in range(vertex_count)]  # [cost, src_set]
    visited = [False for _ in range(vertex_count)]
    queue = []

    paths[0][0] = 0
    heapq.heappush(queue, [0, 0])  # [cost, vertex]

    while len(queue) > 0:
        _, vertex = heapq.heappop(queue)

        if visited[vertex]:
            continue
        visited[vertex] = True

        for next_vertex, next_edge in graph[vertex].items():
            next_cost = paths[vertex][0] + next_edge[0]

            if next_cost > paths[vertex_count-1][0]:
                continue

            if next_cost <= paths[next_vertex][0]:
                if next_cost == paths[next_vertex][0]:
                    paths[next_vertex][1].add(vertex)
                else:
                    paths[next_vertex][0] = next_cost
                    paths[next_vertex][1] = {vertex}

                if next_vertex < vertex_count - 1:
                    heapq.heappush(queue, [next_cost, next_vertex])

    return paths


def trace_path(paths: list, graph: list, goal: int) -> int:
    total_len = 0
    queue = deque()
    queue.append(goal)

    while len(queue) > 0:
        vertex = queue.popleft()

        for src_vertex in paths[vertex][1]:
            queue.append(src_vertex)

            edge = graph[src_vertex][vertex]
            l = edge[0] * edge[1]
            total_len += l

    return total_len * 2


def main():
    P, T = map(int, input().split())

    graph = [{} for _ in range(P)]

    for _ in range(T):
        p1, p2, l = map(int, input().split())

        # {dst: [len, times]}
        # p1 -> p2
        if p2 in graph[p1]:
            edge = graph[p1][p2]
            if l < edge[0]:
                edge[0] = l
                edge[1] = 1
            elif l == edge[0]:
                edge[1] += 1
        else:
            graph[p1][p2] = [l, 1]

        # p2 -> p1
        if p1 != p2:
            if p1 in graph[p2]:
                edge = graph[p2][p1]
                if l < edge[0]:
                    edge[0] = l
                    edge[1] = 1
                elif l == edge[0]:
                    edge[1] += 1
            else:
                graph[p2][p1] = [l, 1]

    paths = dijkstra(graph)
    print(trace_path(paths, graph, P-1))


if __name__ == '__main__':
    main()
