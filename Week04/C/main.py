MAX_VALUE = 1_000_000_000

if __name__ == '__main__':
    N = int(input())

    fees = []
    for _ in range(N):
        fees.append(int(input()))

    dp = [[MAX_VALUE for _ in range(N)] for _ in range(N)]

    dp[0][0] = 0
    dp[1][1] = fees[1]

    for i in range(1, N):  # jump(distance)
        for j in reversed(range(N)):  # square
            if j+i+1 < N:  # forward
                dp[i+1][j+i+1] = min(dp[i][j] + fees[j+i+1], dp[i+1][j+i+1])
            if j >= i:  # backward
                dp[i][j-i] = min(dp[i][j] + fees[j-i], dp[i][j-i])

    cost = MAX_VALUE
    for i in range(N):
        cost = min(dp[i][N-1], cost)

    print(cost)
