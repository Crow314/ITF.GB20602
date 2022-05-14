MAX_VAL = 1_000_000

if __name__ == '__main__':
    n, m = map(int, input().split())

    keyboards = []
    for i in range(n):
        keyboard = list(map(int, input().split()))
        keyboard = keyboard[1:]
        keyboards.append(keyboard)

    notes = list(map(int, input().split()))

    dp = [[MAX_VAL for j in range(n)] for i in range(m)]
    last_min_count = 0

    for j in range(n):
        can_play = False
        for note in keyboards[j]:
            if notes[0] == note:
                can_play = True
                break

        if can_play:
            dp[0][j] = 0

    for i in range(1, m):  # notes
        min_count = MAX_VAL

        for j in range(n):  # current keyboard
            can_play = False
            for note in keyboards[j]:
                if notes[i] == note:
                    can_play = True
                    break

            if can_play:
                dp[i][j] = min(last_min_count+1, dp[i-1][j])

            min_count = min(min_count, dp[i][j])

        last_min_count = min_count

    print(last_min_count)
