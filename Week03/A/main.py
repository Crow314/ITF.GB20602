if __name__ == '__main__':
    R, C = list(map(int, input().split()))
    park = []
    for i in range(R):
        park.append(list(input()))

    answers = [0 for i in range(5)]

    for i in range(R-1):
        for j in range(C-1):
            car_count = 0

            if park[i][j+1] == '#' or park[i+1][j+1] == '#':
                j += 1
                continue
            if park[i][j] == '#' or park[i+1][j] == '#':
                continue

            if park[i][j] == 'X':
                car_count += 1
            if park[i][j+1] == 'X':
                car_count += 1
            if park[i+1][j] == 'X':
                car_count += 1
            if park[i+1][j+1] == 'X':
                car_count += 1

            answers[car_count] += 1

    for ans in answers:
        print(ans)
