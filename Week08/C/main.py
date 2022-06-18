from math import factorial


def main():
    n, m = map(int, input().split())
    # math.comb(n, m-1)
    print(int(factorial(n) / (factorial(m-1) * factorial(n-m+1))))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
