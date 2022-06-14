import bisect


def LIS(seq: list) -> int:
    ans = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > ans[-1]:
            ans.append(seq[i])
        else:
            ans[bisect.bisect_left(ans, seq[i])] = seq[i]

    return len(ans)


def main() -> int:
    _ = input()
    list_p = input().split()
    list_q = input().split()

    dict_p = {}
    for i, v in enumerate(list_p):
        dict_p[v] = i

    common_list = []
    for v in list_q:
        if v in dict_p.keys():
            common_list.append(dict_p[v])

    return LIS(common_list)


if __name__ == '__main__':
    t = int(input())
    for t_i in range(t):
        print('Case ' + str(t_i + 1) + ': ' + str(main()))
