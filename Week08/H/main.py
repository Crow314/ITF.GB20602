def count_prime(n: int, prime: int) -> int:
    count = 0

    while n % prime == 0:
        count += 1
        n //= prime

    return count


def main(n: int):
    ans = 1
    prime2 = 0
    prime5 = 0

    for i in range(2, n+1):
        ans *= i

        prime2 += count_prime(i, 2)
        prime5 += count_prime(i, 5)

        count10 = min(prime2, prime5)
        ans //= 10 ** count10
        prime2 -= count10
        prime5 -= count10

    print(ans % 10)


if __name__ == '__main__':
    while True:
        case = int(input())
        if case == 0:
            break

        main(case)
