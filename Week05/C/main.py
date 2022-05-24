from collections import deque
import copy


def solve(graph, stages, dependencies, n, m, start_lab) -> int:
    lab1_queue = deque()
    lab2_queue = deque()

    for i in range(n):
        if dependencies[i] == 0:
            if stages[i] == 1:
                lab1_queue.append(i)
            else:
                lab2_queue.append(i)

    count = -1
    if start_lab == 1:
        is_lab1 = True
        if len(lab1_queue) == 0:
            return 10 ** 9
    else:
        is_lab1 = False
        if len(lab2_queue) == 0:
            return 10 ** 9

    while (len(lab1_queue) != 0) or (len(lab2_queue) != 0):
        if is_lab1:
            lab_queue = lab1_queue
        else:
            lab_queue = lab2_queue

        while len(lab_queue) > 0:
            stage = lab_queue.popleft()

            for next_stage in graph[stage]:
                dependencies[next_stage] -= 1

                if dependencies[next_stage] > 0:
                    continue

                if stages[next_stage] == 1:
                    lab1_queue.append(next_stage)
                else:
                    lab2_queue.append(next_stage)

        is_lab1 = not is_lab1
        count += 1
    return count


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n, m = map(int, input().split())
        stages = list(map(int, input().split()))

        graph = [[] for _ in range(n)]  # graph[stage][...]
        dependencies = [0 for _ in range(n)]

        for _ in range(m):
            src, dst = map(int, input().split())

            graph[src-1].append(dst-1)
            dependencies[dst-1] += 1

        print(min(solve(graph, stages, copy.copy(dependencies), n, m, 1), solve(graph, stages, copy.copy(dependencies), n, m, 2)))
