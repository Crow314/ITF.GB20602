if __name__ == '__main__':
    data = list(input())

    # policy 1
    count = 0
    if data[0] == "U" and data[1] == "D":
        count = 2
    if data[0] == "D":
        count = 1
    for d in data[2:]:
        if d == "D":
            count += 2
    print(count)

    # policy 2
    count = 0
    if data[0] == "D" and data[1] == "U":
        count = 2
    if data[0] == "U":
        count = 1
    for d in data[2:]:
        if d == "U":
            count += 2
    print(count)

    # policy 3
    count = 0
    for i in range(len(data) - 1):
        if data[i] != data[i+1]:
            count += 1
    print(count)
