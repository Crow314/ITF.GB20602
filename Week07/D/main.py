def cdp(text: str, dp: list, left: int, right: int) -> int:
    if dp[left][right] != -1:  # processed
        return dp[left][right]

    if left == right:
        return 1

    length = right - left + 1
    ans = length

    # Separate
    for i in range(left, right):
        ans = min(ans, cdp(text, dp, left, i) + cdp(text, dp, i+1, right))

    # Power
    for i in range(1, length):
        if length % i == 0:
            flg = True

            for j in range(i, length):
                if text[left+j] != text[left + j%i]:
                    flg = False
                    break

            if flg:
                ans = min(ans, cdp(text, dp, left, left+i-1))

    dp[left][right] = ans
    return dp[left][right]


def main():
    text = input()
    n = len(text)

    dp = [[-1 for _ in range(n)] for _ in range(n)]

    ans = cdp(text, dp, 0, n - 1)
    print(ans)


if __name__ == '__main__':
    main()
