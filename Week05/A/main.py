import sys


def dfs(graph: list, visited: list, visit: int):
    visited[visit] = True

    for next_visit in graph[visit]:
        if not visited[next_visit]:
            dfs(graph, visited, next_visit)


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)  # Only Undirected Graph

    visited = [False for _ in range(N)]

    sys.setrecursionlimit(10 ** 6)
    dfs(graph, visited, 0)

    connected = True
    for i, v in enumerate(visited):
        if not v:
            print(i+1)
            connected = False

    if connected:
        print('Connected')
