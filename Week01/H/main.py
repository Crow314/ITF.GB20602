from typing import List
from sys import stdin

input = stdin.readline


def func1():
    print(7)


def func2(A: List[int]):
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")


def func3(A: List[int]):
    l = A[:3]
    l.sort()
    print(l[1])


def func4(A: List[int]):
    s = 0
    for n in A:
        s += n
    print(s)


def func5(A: List[int]):
    s = 0
    for n in A:
        if n % 2 == 0:
            s += n
    print(s)


def func6(A: List[int]):
    for n in A:
        c = n % 26
        print(chr(c + 0x61), end="")
    print()


def func7(A: List[int]):
    i = 0  # a
    appeared = set()
    while True:  # e1
        appeared.add(i)
        i = A[i]  # b

        if i < 0 or i > N-1:  # c
            print("Out")
            break
        elif i == N-1:  # d
            print("Done")
            break
        elif i in appeared:  # e2
            print("Cyclic")
            break


if __name__ == '__main__':
    N, t = map(int, input().rstrip().split())

    if t == 1:
        func1()
    elif t == 2:
        l = input().rstrip().split(' ', 2)
        A = list(map(int, l[:2]))
        func2(A)
    elif t == 3:
        l = input().rstrip().split(' ', 3)
        A = list(map(int, l[:3]))
        func3(A)
    elif t == 4:
        A = list(map(int, input().split()))
        func4(A)
    elif t == 5:
        A = list(map(int, input().split()))
        func5(A)
    elif t == 6:
        A = list(map(int, input().split()))
        func6(A)
    elif t == 7:
        A = list(map(int, input().split()))
        func7(A)
