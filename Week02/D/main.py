if __name__ == '__main__':
    tmp = list(map(int, input().split()))
    N = tmp[0]
    M = tmp[1]

    time_remaining = []

    for i in range(N):
        time_remaining.append(list(map(int, input().split())))

    time = 0
    stages = [0 for i in range(N)]
    working = [-1 for j in range(M)]
    finished = [0 for i in range(N)]

    while finished[N-1] == 0:
        work_time = 1_000_000

        for j in range(M):
            idle = True
            for i, stage in enumerate(stages):
                if stage == j and time_remaining[i][j] != 0:
                    idle = False
                    working[j] = i
                    work_time = min(time_remaining[i][j], work_time)
                    break
            if idle:
                working[j] = -1

        time += work_time
        for j in range(M):
            i = working[j]
            if i >= 0:
                time_remaining[i][j] -= work_time

                if time_remaining[i][j] <= 0:
                    stages[i] += 1
                    if stages[i] >= M:
                        finished[i] = time

    print(*finished)
