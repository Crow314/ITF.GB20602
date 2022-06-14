def LCS(str1: list, str2: list) -> int:
    dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

    for i, v_i in enumerate(str1):
        for j, v_j in enumerate(str2):
            if v_i == v_j:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    ans = []

    i = len(str1) - 1
    j = len(str2) - 1

    while i >= 0 and j >= 0:
        if str1[i] == str2[j]:
            ans.append(str1[i])
            i -= 1
            j -= 1
        elif dp[i+1][j+1] == dp[i][j+1]:
            i -= 1
        elif dp[i+1][j+1] == dp[i+1][j]:
            j -= 1

    return len(ans)


def main() -> int:
    _ = input()
    str_p = input()
    str_q = input()

    return LCS(str_p.split(), str_q.split())


if __name__ == '__main__':
    t = int(input())
    for t_i in range(t):
        print('Case ' + str(t_i + 1) + ': ' + str(main()))
