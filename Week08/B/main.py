import math


def main():
    N, K = map(int, input().split())

    is_prime = [True for _ in range(N+1)]
    is_prime[0] = False
    is_prime[1] = False

    count = 0
    fin_flg = False

    for p in range(2, N+1):
        if not is_prime[p]:
            continue

        count += 1
        if count == K:
            print(p)
            break

        for i in range(p*p, N+1, p):
            if is_prime[i]:
                is_prime[i] = False

                count += 1
                if count == K:
                    print(i)
                    fin_flg = True
                    break

        if fin_flg:
            break


if __name__ == '__main__':
    main()
