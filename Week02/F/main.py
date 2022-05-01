if __name__ == '__main__':
    N = input()
    M = input()

    result = N

    if M != '1':
        N_len = len(N)
        K_exp = len(M)-1

        # avoid 1/100 -> .1
        if K_exp >= N_len:
            N = ''.join(['0' for x in range(K_exp-N_len+1)]) + N

        result = N[:-K_exp] + '.' + N[-K_exp:]

        # avoid x.0
        length = len(result)
        for i in reversed(range(len(result))):
            if result[i] == '0':
                length = i
            elif result[i] == '.':
                length = i
                break
            else:
                break
        result = result[:length]

    print(result)
