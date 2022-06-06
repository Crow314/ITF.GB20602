from collections import deque

MAX_VALUE = 10 ** 9


def dijkstra(graph: list) -> list:
    paths = [[MAX_VALUE, set()] for _ in range(len(graph))]  # [cost, src_set]
    queue = deque()

    paths[0][0] = 0
    queue.append(0)

    while len(queue) > 0:
        vertex = queue.popleft()

        for next_edge in graph[vertex]:
            next_vertex = next_edge[0]
            next_cost = paths[vertex][0] + next_edge[1]

            if next_cost <= paths[next_vertex][0]:
                if next_cost == paths[next_vertex][0]:
                    paths[next_vertex][1].add(vertex)
                else:
                    paths[next_vertex][0] = next_cost
                    paths[next_vertex][1] = {vertex}
                queue.append(next_vertex)

    return paths


def trace_path(paths: list, graph: list, goal: int) -> int:
    total_len = 0
    queue = deque()
    queue.append(goal)

    while len(queue) > 0:
        vertex = queue.popleft()

        for src_vertex in paths[vertex][1]:
            queue.append(src_vertex)

            for edge in graph[src_vertex]:
                if edge[0] == vertex:
                    total_len += edge[1] * edge[2]

    return total_len * 2


def main():
    P, T = map(int, input().split())

    graph = [[] for _ in range(P)]

    for _ in range(T):
        p1, p2, l = map(int, input().split())

        # [dst, len, times]
        # p1 -> p2
        flg = True
        for edge in graph[p1]:
            if edge[0] == p2:
                flg = False
                if l < edge[1]:
                    edge[1] = l
                    edge[2] = 1
                elif l == edge[1]:
                    edge[2] += 1
        if flg:
            graph[p1].append([p2, l, 1])

        if p1 != p2:
            # p2 -> p1
            flg = True
            for edge in graph[p2]:
                if edge[0] == p1:
                    flg = False
                    if l < edge[1]:
                        edge[1] = l
                        edge[2] = 1
                    if l == edge[1]:
                        edge[2] += 1
            if flg:
                graph[p2].append([p1, l, 1])

    paths = dijkstra(graph)
    print(trace_path(paths, graph, P-1))


if __name__ == '__main__':
    main()
