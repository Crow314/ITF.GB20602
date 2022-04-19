if __name__ == '__main__':
    n1 = int(input())
    n2 = int(input())

    ans = n2 - n1
    ans %= 360
    if ans > 180:
        ans -= 360
    print(ans)
