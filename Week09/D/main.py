import math


def main():
    while True:
        a, b, s, m, n = map(int, input().split())

        if a == b == s == m == n == 0:
            break

        dx = a*m
        dy = b*n

        dist = math.sqrt(dx**2 + dy**2)
        v = dist / s
        A = math.acos(dx / dist)

        print('{:.2f} {:.2f}'.format(math.degrees(A), v))


if __name__ == '__main__':
    main()
