import math
import heapq

MAX_VALUE = 10 ** 10


def dijkstra(graph: dict, n: int, start_time: int) -> int:
    times = [MAX_VALUE for _ in range(n)]
    seen = [False for _ in range(n)]

    queue = []

    times[0] = 0
    heapq.heappush(queue, [start_time, 0])  # [time_arrival, u]

    while queue:
        time_arrival, u = heapq.heappop(queue)

        if seen[u]:
            continue
        seen[u] = True

        if u == n-1:
            break

        if u not in graph:
            continue

        for v, t0, p, d in graph[u]:
            if time_arrival < t0:
                time_departure = t0
            else:
                time_departure = math.floor((time_arrival - t0 + p - 1) / p) * p + t0

            eta = time_departure + d

            if eta < times[v]:
                times[v] = eta
                heapq.heappush(queue, [eta, v])

    return times[n-1]


def main():
    n, m, s = map(int, input().split())

    trams = {}

    for _ in range(m):
        u, v, t0, p, d = map(int, input().split())

        if u not in trams:
            trams[u] = []

        trams[u].append([v, t0, p, d])

    if dijkstra(trams, n, 0) <= s:
        left = 0
        right = s

        while left < right:
            mid = math.ceil((left + right) / 2)

            if dijkstra(trams, n, mid) > s:
                right = mid - 1
            else:
                left = mid

        print(left)

    else:
        print('impossible')


if __name__ == '__main__':
    main()
