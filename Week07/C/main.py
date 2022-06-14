def main():
    n = int(input())

    numbers = []

    flg = True

    for _ in range(n):
        number = input()
        l = len(number)

        for exist in numbers:
            exist_l = len(exist)
            if exist_l > l:
                if exist[:l] == number:
                    flg = False
                    break
            else:
                if number[:exist_l] == exist:
                    flg = False
                    break

        if not flg:
            break

        numbers.append(number)

    res = 'YES' if flg else 'NO'
    print(res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        main()
