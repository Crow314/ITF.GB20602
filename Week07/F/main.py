def main(string: str):
    str_len = len(string)
    ans = 0

    for i in range(1, str_len+1):
        if str_len % i != 0:
            continue

        ans = int(str_len / i)
        substr = string[:i]

        if substr * ans == string:
            break

    print(ans)


if __name__ == '__main__':
    while True:
        s = input()
        if '.' in s:
            break

        main(s)
