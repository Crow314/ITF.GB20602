import math

if __name__ == '__main__':
    line = input()
    maxN = 0
    while True:
        if line == "0":
            break
        n, k = map(int, line.split())
        maxN = max(n, maxN)
        results = [[0 for j in range(2)] for i in range(maxN)]

        for i in range(math.ceil(k * n * (n-1) / 2)):
            p1, m1, p2, m2 = input().split()
            if m1 == m2:
                pass
            elif (m1 == "rock" and m2 == "scissors") \
                    or (m1 == "scissors" and m2 == "paper") \
                    or (m1 == "paper" and m2 == "rock"):
                results[int(p1)-1][0] += 1
                results[int(p2)-1][1] += 1
            else:
                results[int(p1)-1][1] += 1
                results[int(p2)-1][0] += 1

        for i in range(n):
            match_count = results[i][0]+results[i][1]
            if match_count != 0:
                print(format(round(results[i][0]/match_count, 3), ".3f"))
            else:
                print("-")

        line = input()
        if line != "0":
            print()
