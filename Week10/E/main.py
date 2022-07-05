import sys
import heapq

input = sys.stdin.readline
MAX_VALUE = 10 ** 10


def dijkstra(graph: list, times: list, seen: list, n: int, start_time: int) -> int:
    for i in range(n):
        times[i] = MAX_VALUE
        seen[i] = False

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

        for v, t0, p, d in graph[u]:
            if time_arrival < t0:
                time_departure = t0
            else:
                time_departure = (time_arrival - t0 + p - 1) // p * p + t0

            eta = time_departure + d

            if eta < times[v]:
                times[v] = eta
                heapq.heappush(queue, [eta, v])

    return times[n-1]


def main():
    n, m, s = map(int, input().split())

    trams = [[] for _ in range(m)]

    for _ in range(m):
        u, v, t0, p, d = map(int, input().split())

        trams[u].append([v, t0, p, d])

    times = [MAX_VALUE for _ in range(n)]
    seen = [False for _ in range(n)]

    if dijkstra(trams, times, seen, n, 0) <= s:
        left = 0
        right = s

        while left < right:
            mid = (left + right) // 2 + (left + right) % 2

            if dijkstra(trams, times, seen, n, mid) > s:
                right = mid - 1
            else:
                left = mid

        print(left)

    else:
        print('impossible')


if __name__ == '__main__':
    main()
