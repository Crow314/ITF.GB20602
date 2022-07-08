import math


def main():
    n = int(input())

    op = []
    unknown_op = None

    flg = True

    for _ in range(n):
        opcode, operand = input().split()

        if operand != '?':
            op.append([opcode, int(operand)])
        else:
            unknown_op = opcode
            op.append([opcode, None])

    pos = [0, 0]
    direction = 0

    unknown_pos = None

    for opcode, operand in op:
        if operand is not None:
            if opcode in ['bk', 'rt']:
                operand *= -1

            if opcode in ['fd', 'bk']:
                rad = math.radians(direction)
                pos[0] += operand * math.cos(rad)  # dx
                pos[1] += operand * math.sin(rad)  # dy
            else:
                direction += operand
                direction %= 360
        else:
            unknown_pos = pos.copy()

    if unknown_op in ['fd', 'bk']:
        dist = math.sqrt(pos[0] ** 2 + pos[1] ** 2)
        print(round(dist))

    else:
        vec1 = [-unknown_pos[0], -unknown_pos[1]]
        vec2 = [pos[0] - unknown_pos[0], pos[1] - unknown_pos[1]]

        dist1 = math.sqrt(vec1[0] ** 2 + vec1[1] ** 2)
        dist2 = math.sqrt(vec2[0] ** 2 + vec2[1] ** 2)

        if (dist1 != 0) and (dist2 != 0):
            inner_prod = vec1[0]*vec2[0] + vec1[1]*vec2[1]

            theta = math.acos(inner_prod/(dist1 * dist2))
            angle = round(math.degrees(theta))

            cross_prod = vec2[0]*vec1[1] - vec2[1]*vec1[0]  # vec2 X vec1
            if cross_prod < 0:
                angle *= -1

            if unknown_op == 'lt':
                print(angle % 360)
            else:
                print((360 - angle) % 360)
        else:
            print(0)


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        main()
