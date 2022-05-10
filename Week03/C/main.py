import math

if __name__ == '__main__':
    N, M, K = list(map(int, input().split()))
    plots = list(map(int, input().split()))
    houses = list(map(int, input().split()))
    square_houses = list(map(int, input().split()))

    for h in square_houses:
        houses.append(h / math.sqrt(2))

    plots.sort()
    houses.sort()

    count = 0
    house_idx = 0
    for plot in plots:
        if house_idx >= len(houses):
            break

        if plot > houses[house_idx]:
            house_idx += 1
            count += 1

    print(count)
