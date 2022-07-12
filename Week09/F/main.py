import math


def calc_angle(corners: list, center: int, prev: int, next: int) -> float:
    n = len(corners)

    o = corners[center % n]
    p1 = corners[prev % n]
    p2 = corners[next % n]

    dx1 = p1[0] - o[0]
    dy1 = p1[1] - o[1]
    dx2 = p2[0] - o[0]
    dy2 = p2[1] - o[1]

    angle = math.atan2(dy2, dx2) - math.atan2(dy1, dx1)
    if angle < 0:
        angle += 2 * math.pi

    return math.degrees(angle)


def main():
    while True:
        line = list(map(int, input().split()))
        n = line[0]

        if n == 0:
            break

        corners = []

        for i in range(1, len(line), 2):
            corners.append([line[i], line[i+1]])  # [X, Y]

        angles = [-1 for _ in range(n)]

        for i in range(n):
            angles[i % n] = calc_angle(corners, i, i-1, i+1)

        while len(corners) >= 4:
            min_angle = 180
            min_idx = 0
            sum_angle = 0

            for i in range(len(corners)):
                if angles[i % n] < min_angle:
                    min_angle = angles[i % n]
                    min_idx = i % n
                sum_angle += angles[i % n]

            angle_prev = calc_angle(corners, min_idx-1, min_idx-2, min_idx+1)
            angle_next = calc_angle(corners, min_idx+1, min_idx-1, min_idx+2)

            if (angle_prev <= min_angle) or (angle_next <= min_angle):
                break
            else:
                angles[min_idx-1] = angle_prev
                angles[min_idx+1] = angle_next

                corners.pop(min_idx)
                angles.pop(min_idx)

        print(str(len(corners)), end='')
        for corner in corners:
            print(' {} {}'.format(corner[0], corner[1]), end='')
        print()


if __name__ == '__main__':
    main()
