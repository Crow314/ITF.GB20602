import bisect


class Doll:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return (self.width == other.width) and (self.height == other.height)

    def __lt__(self, other):
        return (self.width < other.width) if (self.width != other.width) else (self.height > other.height)

    def __gt__(self, other):
        return (self.width > other.width) if (self.width != other.width) else (self.height < other.height)

    def __le__(self, other):
        return (self.width < other.width) if (self.width != other.width) else (self.height >= other.height)

    def __ge__(self, other):
        return (self.width > other.width) if (self.width != other.width) else (self.height <= other.height)


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        m = int(input())
        tmp = list(map(int, input().split()))

        dolls = []

        for i in range(0, m):
            doll = Doll(tmp[i*2], tmp[i*2 + 1])
            dolls.append(doll)

        dolls.sort()
        seq = []

        for doll in dolls:
            seq.append(doll)

        LDS = [seq[0]]
        for i in range(1, len(seq)):
            if seq[i].height <= LDS[-1].height:
                LDS.append(seq[i])
            else:
                LDS[bisect.bisect_right(LDS, seq[i])-1] = seq[i]

        print(len(LDS))
