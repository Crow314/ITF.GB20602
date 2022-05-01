if __name__ == '__main__':
    tmp = list(map(int, input().split()))
    N = tmp[0]
    M = tmp[1]

    times = []
    for i in range(N):
        times.append(list(map(int, input().split())))

    finished = [[1_000_000_000_000 for j in range(M)] for i in range(N)]
    finished[0][0] = times[0][0]

    # i=0
    for j in range(1, M):
        finished[0][j] = finished[0][j-1] + times[0][j]

    # i>0, j=0
    for i in range(1, N):
        finished[i][0] = finished[i-1][0] + times[i][0]

    # i>0, j>0
    for i in range(1, N):
        for j in range(1, M):
            finished[i][j] = max(finished[i-1][j], finished[i][j-1]) + times[i][j]

    for i in range(N):
        print(finished[i][M-1], end='')
        if i < N-1:
            print(' ', end='')
