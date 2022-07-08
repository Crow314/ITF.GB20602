import bisect
import math


def main():
    n, interval = map(int, input().split())

    corners = []
    times = []

    for _ in range(n):
        x, y, t = map(int, input().split())
        corners.append([x, y])
        times.append(t)

    gps_pos = []

    time = 0
    while True:
        edge_idx = bisect.bisect_right(times, time) - 1

        if edge_idx == n-1:
            gps_pos.append(corners[edge_idx])
            break

        dx = (corners[edge_idx + 1][0] - corners[edge_idx][0]) / (times[edge_idx + 1] - times[edge_idx]) * (time - times[edge_idx])  # v * t
        dy = (corners[edge_idx + 1][1] - corners[edge_idx][1]) / (times[edge_idx + 1] - times[edge_idx]) * (time - times[edge_idx])  # v * t

        gps_x = dx + corners[edge_idx][0]
        gps_y = dy + corners[edge_idx][1]

        gps_pos.append([gps_x, gps_y])

        time += interval

    distance = 0
    for i in range(n-1):
        distance += math.sqrt((corners[i+1][0] - corners[i][0])**2 + (corners[i+1][1] - corners[i][1])**2)

    gps_distance = 0

    for i in range(len(gps_pos)-1):
        gps_distance += math.sqrt((gps_pos[i+1][0] - gps_pos[i][0])**2 + (gps_pos[i+1][1] - gps_pos[i][1])**2)

    ans = abs(gps_distance - distance) / distance * 100
    print(ans)


if __name__ == '__main__':
    main()
