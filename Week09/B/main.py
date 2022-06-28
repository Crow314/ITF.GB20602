import math


def main(r: int, h: int, s: int):
    angle = 2 * (math.pi - math.acos(r/h))  # 2Pi - acos * 2

    ans = 2 * math.sqrt(h*h - r*r)
    ans += angle * r

    ans *= (s + 100) / 100

    print('{0:.2f}'.format(ans))


if __name__ == '__main__':
    while True:
        r, h, s = map(int, input().split())
        if r == 0:
            break

        main(r, h, s)
