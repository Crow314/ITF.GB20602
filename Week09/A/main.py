import heapq


def main():
    N = int(input())

    pf_list = []

    for _ in range(N):
        Y, X1, X2 = map(int, input().split())
        heapq.heappush(pf_list, [Y, X1, X2])

    levels = [0 for _ in range(10001)]
    ans = 0

    while len(pf_list):
        Y, X1, X2 = heapq.heappop(pf_list)

        ans += Y - levels[X1]
        ans += Y - levels[X2-1]

        for i in range(X1, X2):
            levels[i] = Y

    print(ans)


if __name__ == '__main__':
    main()
