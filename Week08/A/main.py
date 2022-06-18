import math


def main():
    _ = int(input())
    rings = list(map(int, input().split()))

    numerator = 1
    denominator = 1

    for i in range(len(rings)-1):
        numerator *= rings[i]
        denominator *= rings[i+1]

        gcd = math.gcd(numerator, denominator)
        numerator = int(numerator/gcd)
        denominator = int(denominator/gcd)

        print(str(numerator) + '/' + str(denominator))


if __name__ == '__main__':
    main()
