def LCS(str1: list, str2: list) -> int:
    dp = [[0 for _ in range(len(str2)+1)] for _ in range(2)]

    for i, v_i in enumerate(str1):
        for j, v_j in enumerate(str2):
            if v_i == v_j:
                dp[1][j+1] = dp[0][j] + 1
            else:
                dp[1][j+1] = max(dp[1][j], dp[0][j+1])

        dp[0] = dp[1]

    return dp[0][len(str2)]


def main() -> int:
    _ = input()
    str_p = input()
    str_q = input()

    return LCS(str_p.split(), str_q.split())


if __name__ == '__main__':
    t = int(input())
    for t_i in range(t):
        print('Case ' + str(t_i + 1) + ': ' + str(main()))
