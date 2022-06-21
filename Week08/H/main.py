def solve() -> list:
    MAX = 1_000_000

    answers = [-1 for _ in range(MAX)]
    answers[0] = 1
    ans = 1

    for i in range(2, MAX+1):
        ans *= i
        while ans % 10 == 0:
            ans //= 10

        answers[i-1] = ans % 10
        ans %= MAX

    return answers


def main(answers: list, n: int):
    print(answers[n-1] % 10)


if __name__ == '__main__':
    answers = solve()

    while True:
        case = int(input())
        if case == 0:
            break

        main(answers, case)
