def main(k: int, n: int):
    words = pow(k+1, n)

    dp = [[0 for _ in range(k+1)] for _ in range(n)]

    for j in range(k+1):
        dp[0][j] = 1

    for i in range(1, n):
        for j in range(k+1):
            for last_j in range(max(j-1, 0), min(j+1, k)+1):
                dp[i][j] += dp[i-1][last_j]

    count = 0
    for j in range(k+1):
        count += dp[n-1][j]

    print(100.0 * count / words)


if __name__ == '__main__':
    while True:
        try:
            k, n = map(int, input().split())
            main(k, n)
        except EOFError:
            break
