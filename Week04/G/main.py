import math


def combination(n: int, r: int) -> int:
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


if __name__ == '__main__':
    g = int(input())

    for game in range(g):
        m = int(input())
        tiles = list(map(int, input().split()))
        n, t = map(int, input().split())

        dp = [[[0 for _ in range(t+1)] for _ in range(n+2)] for _ in range(m+1)]

        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n+1):
                for k in range(t+1):
                    # pick
                    dp[i+1][j][k] += dp[i][j][k]

                    # no pick
                    next_k = k + tiles[i]
                    if next_k > t:
                        continue

                    dp[i+1][j+1][next_k] += dp[i][j][k]

        count = dp[m][n][t]

        combination_count = combination(m, n)

        print('Game ' + str(game + 1) + ' -- ' + str(count) + ' : ' + str(combination_count - count))
