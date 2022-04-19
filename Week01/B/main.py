if __name__ == '__main__':
    X = int(input())
    N = int(input())
    spent = 0

    for i in range(N):
        P = int(input())
        spent += P

    print(X*(N+1) - spent)
