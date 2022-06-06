MIN_VALUE = 0


def floyd_warshall(graph: list):
    V = len(graph)

    for k in range(V):
        for src in range(V):
            for dst in range(V):
                graph[src][dst] = max(graph[src][dst], graph[src][k] * graph[k][dst])


def has_arbitrage_cycle(graph: list) -> bool:
    floyd_warshall(graph)

    for i in range(len(graph)):
        if graph[i][i] > 1:
            return True

    return False


def main(C: int):
    codes = input().split()
    code_dict = {}
    code_count = 0
    for code in codes:
        code_dict[code] = code_count
        code_count += 1

    graph = [[MIN_VALUE for _ in range(C)] for _ in range(C)]

    for i in range(C):
        graph[i][i] = 1.0

    R = int(input())

    for _ in range(R):
        strings = input().split()
        A_code = strings[0]
        B_code = strings[1]
        A, B = map(int, strings[2].split(sep=':'))

        graph[code_dict[A_code]][code_dict[B_code]] = 1.0 * B / A

    if has_arbitrage_cycle(graph):
        print('Arbitrage')
    else:
        print('Ok')


if __name__ == '__main__':
    while True:
        c = int(input())
        if c == 0:
            break
        main(c)
