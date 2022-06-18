def divisors(n: int) -> list:
    lower_divisors, upper_divisors = [], []

    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1

    return (lower_divisors + list(reversed(upper_divisors)))[:-1]


def main(p: int):
    divs = divisors(p)

    s = sum(divs)

    if s == p:
        print(str(p) + ' perfect')
    elif p-2 <= s <= p+2:
        print(str(p) + ' almost perfect')
    else:
        print(str(p) + ' not perfect')


if __name__ == '__main__':
    while True:
        try:
            main(int(input()))
        except EOFError:
            break
