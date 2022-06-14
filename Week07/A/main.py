def main():
    friend_correct = int(input())

    my_ans = list(input())
    friend_ans = list(input())

    count = len(my_ans)
    friend_wrong = count - friend_correct

    same = 0
    different = 0

    for i in range(count):
        if my_ans[i] == friend_ans[i]:
            same += 1
        else:
            different += 1

    print(min(same, friend_correct) + min(different, friend_wrong))


if __name__ == '__main__':
    main()
