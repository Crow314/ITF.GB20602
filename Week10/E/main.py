def main():
    n, m, s = map(int, input().split())

    schedule = {}

    for _ in range(m):
        u, v, t0, p, d = map(int, input().split())

        i = 0
        while True:
            departure = p * i + t0
            arrival = departure + d

            if arrival > s:
                break

            if arrival not in schedule:
                schedule[arrival] = []

            schedule[arrival].append([u, v, departure])

            i += 1

    dp = [-1 for _ in range(n)]
    dp[n-1] = s

    for i in reversed(range(s)):
        if i not in schedule:
            continue

        for tram in schedule[i]:
            u, v, departure = tram

            if dp[v] > departure:
                dp[u] = max(departure, dp[u])

    if dp[0] >= 0:
        print(dp[0])
    else:
        print('impossible')


if __name__ == '__main__':
    main()
