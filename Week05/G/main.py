from collections import deque


def bfs(graph: list, groups: list, host: int) -> bool:
    groups[host] = 1

    bfs_queue = deque()
    bfs_queue.append(host)

    bipartite = True

    while len(bfs_queue) > 0:
        host = bfs_queue.popleft()
        group = groups[host]

        for next_host in graph[host]:
            next_group = groups[next_host]

            if next_group == 0:
                if group == 1:
                    next_group = 2
                else:
                    next_group = 1

                bfs_queue.append(next_host)
                groups[next_host] = next_group
            elif next_group == group:
                bipartite = False

    return bipartite


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    groups = [False for _ in range(N)]  # 0: not queued / 1: Group1 / 2: Group2

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)  # Undirected Graph

    count = -1
    has_not_bipartite = False
    for i in range(N):
        if groups[i] != 0:
            continue

        bipartite = bfs(graph, groups, i)

        if not bipartite:
            has_not_bipartite = True

        count += 1

    if not has_not_bipartite:
        count += 1

    print(count)
