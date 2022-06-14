from collections import deque


def main():
    n = int(input())

    numbers = []

    for _ in range(n):
        numbers.append(input())

    numbers.sort(key=len)
    queue = deque(numbers)

    flg = True

    for _ in range(n):
        target = queue.popleft()
        l = len(target)

        for number in queue:
            if number[:l] == target:
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
