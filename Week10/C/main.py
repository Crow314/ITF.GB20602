import math
from collections import deque


def main():
    n = int(input())

    gears = []

    for _ in range(n):
        x, y, r = map(int, input().split())
        gears.append([x, y, r])

    connections = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            if ((gears[i][0] - gears[j][0])**2 + (gears[i][1] - gears[j][1])**2) == (gears[i][2] + gears[j][2])**2:
                connections[i].append(j)
                connections[j].append(i)

    ratios = {0: [1, 1]}  # [numerator, denominator]
    queue = deque()

    if len(connections[0]) > 0:
        queue.append(0)

    can_move = True

    while queue:
        gear1 = queue.popleft()

        for gear2 in connections[gear1]:
            ratio_numer = ratios[gear1][0] * gears[gear1][2] * -1
            ratio_denom = ratios[gear1][1] * gears[gear2][2]

            gcd = math.gcd(ratio_numer, abs(ratio_denom))

            ratio_numer //= gcd
            ratio_denom //= gcd

            if gear2 not in ratios:
                ratios[gear2] = [ratio_numer, ratio_denom]
                queue.append(gear2)
                continue

            if (ratios[gear2][0] != ratio_numer) or (ratios[gear2][1] != ratio_denom):
                can_move = False

        if not can_move:
            break

    if n-1 not in ratios:
        print(0)
    elif not can_move:
        print(-1)
    else:
        print(str(ratios[n-1][1]) + ' ' + str(ratios[n-1][0]))


if __name__ == '__main__':
    main()
