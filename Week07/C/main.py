def main():
    n = int(input())

    root = {}

    consistent = True

    for _ in range(n):
        number = list(map(int, list(input())))
        l = len(number)
        parent_node = root

        for i in range(l):
            c = number[i]

            if c in parent_node.keys():
                node = parent_node[c]

                if -1 in node.keys():
                    consistent = False
                    break

                if i == l-1:  # last char
                    if (-1 not in node.keys()) and (len(node) > 0):  # has next node
                        consistent = False
                        break
                    node[-1] = None
                else:
                    parent_node = node

            else:
                parent_node[c] = {}
                node = parent_node[c]

                if i == l-1:  # last char
                    node[-1] = None
                else:
                    parent_node = node

        if not consistent:
            break

    res = 'YES' if consistent else 'NO'
    print(res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        main()
