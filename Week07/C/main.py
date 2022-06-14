import heapq


def main():
    n = int(input())

    numbers = []

    for _ in range(n):
        number = input()
        numbers.append([len(number), number])

    heapq.heapify(numbers)

    flg = True

    for _ in range(n):
        _, target = heapq.heappop(numbers)
        l = len(target)

        for number in numbers:
            if number[1][:l] == target:
                flg = False
                break

        if not flg:
            break

    res = 'YES' if flg else 'NO'
    print(res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        main()
