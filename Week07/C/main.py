def main():
    n = int(input())

    graph = {}  # i*10+j: set() / i文字目がjのときの後続文字

    flg = True

    for _ in range(n):
        number = list(map(int, list(input())))
        l = len(number)
        key = 0

        for i in range(l):
            c = number[i]
            key = key * 10 + c

            if key not in graph.keys():
                graph[key] = set()

            if -1 in graph[key]:
                flg = False
                break

            if (i == l-1) or (i == 9):
                if (-1 not in graph[key]) and (len(graph[key]) > 0):
                    flg = False
                    break
                graph[key].add(-1)
            else:
                graph[key].add(key*10 + number[i+1])

        if not flg:
            break

    res = 'YES' if flg else 'NO'
    print(res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        main()
