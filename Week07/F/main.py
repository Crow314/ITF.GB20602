def main(string: str):
    str_len = len(string)
    ans = 0

    for i in range(1, str_len+1):
        if str_len % i != 0:
            continue

        ans = int(str_len / i)
        substr1 = string[:i]

        flg = True
        for j in reversed(range(1, ans)):
            substr2 = string[i*j: i*(j+1)]

            if substr1 != substr2:
                flg = False
                break

        if flg:
            break

    print(ans)


if __name__ == '__main__':
    while True:
        s = input()
        if s == '.':
            break

        main(s)
