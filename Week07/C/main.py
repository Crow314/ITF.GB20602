def main():
    n = int(input())

    root = {}

    consistent = True

    for _ in range(n):
        number = list(map(int, list(input())))
        l = len(number)
        node = root

        for i in range(l):
            c = number[i]

            if c not in node.keys():
                node[c] = {}
            next_node = node[c]

            if -1 in next_node.keys():
                consistent = False
                break

            if i == l-1:  # last char
                if (-1 not in next_node.keys()) and (len(next_node) > 0):  # has next node
                    consistent = False
                    break
                next_node[-1] = None
            else:
                node = next_node

        if not consistent:
            break

    res = 'YES' if consistent else 'NO'
    print(res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        main()
