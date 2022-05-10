import sys
from collections import deque

if __name__ == '__main__':
    lines = deque()
    for line in sys.stdin.readlines():
        lines.append(line.rstrip())

    case = 0
    while len(lines) > 0:
        case += 1

        n = int(lines.popleft())
        numbers = []
        for i in range(n):
            numbers.append(int(lines.popleft()))

        m = int(lines.popleft())
        queries = []
        for i in range(m):
            queries.append(int(lines.popleft()))

        sums = []
        for i in range(n):
            for j in range(0+i, n):
                if numbers[i] != numbers[j]:
                    sums.append(numbers[i] + numbers[j])
        sums.sort()

        print('Case ' + str(case) + ':')

        for query in queries:
            left = 0
            right = len(sums)

            while True:
                if left >= len(sums):
                    idx = len(sums) - 1
                    break
                if right < 0:
                    idx = 0
                    break
                if left > right:
                    idx = left
                    break

                idx = int((left + right) / 2)
                if sums[idx] == query:
                    break
                if sums[idx] < query:
                    left = idx+1
                    continue
                if sums[idx] > query:
                    right = idx-1
                    continue

            answers = [[sums[idx], 0]]
            if idx > 0:
                answers.append([sums[idx-1], 0])
            if idx < len(sums)-1:
                answers.append([sums[idx+1], 0])

            for ans in answers:
                ans[1] = abs(ans[0] - query)
            answers.sort(key=lambda x: x[1])

            print('Closest sum to ' + str(query) + ' is ' + str(answers[0][0]) + '.')
