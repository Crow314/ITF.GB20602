import sys


def dfs(graph: list, groups: list, host: int, group: int, not_bipartite: bool) -> bool:
    groups[host] = group

    for next_host in graph[host]:
        next_group = groups[next_host]
        if next_group == 0:
            if group == 1:
                next_group = 2
            else:
                next_group = 1

            not_bipartite = dfs(graph, groups, next_host, next_group, not_bipartite)
        elif next_group == group:
            not_bipartite = True

    return not_bipartite


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    groups = [False for _ in range(N)]  # 0: not visited / 1: Group1 / 2: Group2

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)  # Undirected Graph

    sys.setrecursionlimit(M * 10)

    count = -1
    has_not_bipartite = False
    while True:
        try:
            host = groups.index(False)
            not_bipartite = dfs(graph, groups, host, 1, False)

            if not_bipartite:
                has_not_bipartite = True
        except ValueError:
            break

        count += 1

    if not has_not_bipartite:
        count += 1

    print(count)
