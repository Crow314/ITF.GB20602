import math
from collections import deque


def adj_list(rooms: list) -> list:
    n = len(rooms)
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            cap = math.gcd(rooms[i], rooms[j])
            if cap > 1:
                edge1 = [j, cap, None]
                edge2 = [i, cap, edge1]
                edge1[2] = edge2

                graph[i].append(edge1)
                graph[j].append(edge2)

    return graph


def bfs(graph: list, source: int, sink: int) -> list:
    n = len(graph)
    levels = [-1 for _ in range(n)]
    bfs_queue = deque()

    levels[source] = 0
    bfs_queue.append(source)

    while len(bfs_queue) > 0:
        vertex = bfs_queue.popleft()
        next_level = levels[vertex] + 1

        for next_vertex, cap, _ in graph[vertex]:
            if (levels[next_vertex] == -1) and (cap > 0):
                levels[next_vertex] = next_level
                bfs_queue.append(next_vertex)

    return levels


def dfs(graph: list, levels: list, iterator: list, vertex: int, sink: int, flow: int) -> int:
    if vertex == sink:
        return flow

    for i in range(max(iterator[vertex] - 1, 0), len(graph[vertex])):
        iterator[vertex] = i
        edge = graph[vertex][i]
        dst, cap, rev_edge = edge

        if levels[dst] != levels[vertex] + 1:
            continue

        if levels[vertex] < levels[dst]:
            f = dfs(graph, levels, iterator, dst, sink, min(flow, cap))
            if f != 0:
                edge[1] -= f
                rev_edge[1] += f
                return f

    return 0


def max_flow(graph: list, source: int, sink: int) -> int:  # Dinic's algorithm
    flow = 0
    INF = 10 ** 10

    while True:
        levels = bfs(graph, source, sink)
        if levels[sink] == -1:
            break

        itr = [0 for _ in range(len(graph))]
        f = INF
        while f != 0:
            f = dfs(graph, levels, itr, source, sink, INF)
            flow += f

    return flow


def main():
    n = int(input())

    rooms = []
    min_vertex = 10 ** 10
    max_vertex = 0

    start = None
    goal = None

    for i in range(n):
        weight = int(input())
        rooms.append(weight)

        if weight < min_vertex:
            min_vertex = weight
            start = i

        if weight > max_vertex:
            max_vertex = weight
            goal = i

    graph = adj_list(rooms)
    print(max_flow(graph, start, goal))


if __name__ == '__main__':
    main()
