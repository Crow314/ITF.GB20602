def prime_factorize(n: int):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    f = 3
    while f * f <= n:
        if n % f == 0:
            factors.append(f)
            n //= f
        else:
            f += 2

    if n != 1:
        factors.append(n)
    return factors


def main(n: int, k: int):
    dic = {}

    for i in range(k):
        for factor in prime_factorize(n-i):
            if factor not in dic:
                dic[factor] = 0
            dic[factor] += 1

    for i in range(k):
        for factor in prime_factorize(i+1):
            dic[factor] -= 1

    ans = 1
    for a in dic.values():
        ans *= a + 1

    print(ans)


if __name__ == '__main__':
    while True:
        try:
            n, k = map(int, input().split())
            main(n, k)
        except EOFError:
            break
