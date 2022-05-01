if __name__ == '__main__':
    N = int(input())
    baloons = list(map(int, input().split()))

    arrows = [0 for i in range(1_000_000)]
    count = 0

    for v in baloons:
        if arrows[v] > 0:
            arrows[v] -= 1
        else:
            count += 1

        if v > 1:
            arrows[v-1] += 1

    print(count)
