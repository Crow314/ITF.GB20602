import math
import heapq
from collections import deque

MAX_VALUE = 10 ** 14 + 1
MAX_T = 10 ** 9


def dijkstra(graph: dict, city_quantity: int, general_limit: float, edge_limit: int) -> int:
    n = city_quantity

    paths = [MAX_VALUE for _ in range(n)]
    seen = [False for _ in range(n)]

    queue = []

    paths[0] = 0
    heapq.heappush(queue, [0, 0])  # [cost, vertex]

    while queue:
        _, vertex = heapq.heappop(queue)

        if seen[vertex]:
            continue
        seen[vertex] = True

        if vertex == n-1:
            break

        for next_v, T in graph[vertex]:
            if T > edge_limit:
                continue

            cost = paths[vertex] + T

            if (cost < paths[next_v]) and (cost <= general_limit):
                paths[next_v] = cost
                heapq.heappush(queue, [cost, next_v])

    return paths[n-1]


def main():
    N, M, X = map(int, input().split())

    highways = {}

    for _ in range(M):
        C1, C2, T = map(int, input().split())

        C1 -= 1
        C2 -= 1

        if C1 not in highways:
            highways[C1] = []
        if C2 not in highways:
            highways[C2] = []

        highways[C1].append([C2, T])
        highways[C2].append([C1, T])

    limit = dijkstra(highways, N, MAX_VALUE, MAX_T) * (100 + X) / 100

    left = 0
    right = MAX_T
    ans = -1

    while left < right:
        mid = math.ceil((left+right)/2)

        if dijkstra(highways, N, limit, mid) < MAX_VALUE:
            ans = mid
            right = mid - 1
        else:
            left = mid

    print(ans)


if __name__ == '__main__':
    main()
