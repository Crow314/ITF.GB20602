if __name__ == '__main__':
    word = input()
    ans = word

    for i in range(1, len(word)-1):
        for j in range(i+1, len(word)):
            tmp = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
            if ans > tmp:
                ans = tmp

    print(ans)
