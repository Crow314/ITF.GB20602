def main():
    m = int(input())

    cubics = []

    # cbrt(400000) -> 73.7
    for i in range(1, 74):
        cubic = i ** 3
        if cubic >= m:
            break
        cubics.append(cubic)

    ans = -1
    seen = {}

    for i in range(len(cubics)):
        for j in range(0, i):
            tmp = cubics[i] + cubics[j]

            if tmp > m:
                break

            if tmp in seen:
                ans = max(tmp, ans)
            else:
                seen[tmp] = True

    print(ans if ans > -1 else 'none')


if __name__ == '__main__':
    main()
