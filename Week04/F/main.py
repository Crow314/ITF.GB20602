RECORD_LENGTH = 1440
COST = -8

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break

        profits = [COST for _ in range(RECORD_LENGTH)]

        for _ in range(n):
            time, profit = input().split()
            time = int(time)
            profit = int(round(float(profit) * 100))

            profits[time] += profit

        dp = [[[COST, 0, 0] for _ in range(2)] for _ in range(RECORD_LENGTH)]  # [minutes][0:opened, 1:closed][0:profit, 1:begin, 2:end]

        for i in range(RECORD_LENGTH):
            profit = profits[i]

            if i > 0:
                dp[i][0][0] = dp[i-1][0][0] + profit
                dp[i][0][1] = dp[i-1][0][1]

                dp[i][1][0] = dp[i-1][1][0]
                dp[i][1][1] = dp[i-1][1][1]
                dp[i][1][2] = dp[i-1][1][2]

            if profit > dp[i][0][0]:
                dp[i][0] = [profit, i, -1]

            if dp[i][0][0] > dp[i-1][1][0]:
                dp[i][1] = [dp[i][0][0], dp[i][0][1], i]

            if (dp[i][0][0] == dp[i-1][1][0]) and ((i - dp[i][0][1]) < (dp[i-1][1][2] - dp[i-1][1][1])):
                dp[i][1] = [dp[i][0][0], dp[i][0][1], i]

        if dp[RECORD_LENGTH-1][1][0] > 0:
            print('{:.2f}'.format(round(dp[RECORD_LENGTH-1][1][0] / 100, 2)) + ' ' + str(dp[RECORD_LENGTH-1][1][1]) + ' ' + str(dp[RECORD_LENGTH-1][1][2]))
        else:
            print('no profit')
