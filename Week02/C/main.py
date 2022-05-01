if __name__ == '__main__':
    for case in range(int(input())):
        selling = [0 for i in range(1001)]
        buying = [0 for i in range(1001)]

        ask = 1001
        bid = 0
        stock = '-'

        for i in range(int(input())):
            line = input().split()

            if line[0] == 'sell':
                amount = int(line[1])
                price = int(line[4])

                for j in reversed(range(price, bid+1)):
                    trade_amount = min(amount, buying[j])
                    amount -= trade_amount
                    buying[j] -= trade_amount

                    if trade_amount != 0:
                        stock = price

                selling[price] += amount

            if line[0] == 'buy':
                amount = int(line[1])
                price = int(line[4])

                for j in range(ask, price+1):
                    trade_amount = min(amount, selling[j])
                    amount -= trade_amount
                    selling[j] -= trade_amount

                    if trade_amount != 0:
                        stock = j

                buying[price] += amount

            flg = True
            for j, v in enumerate(selling):
                if v != 0:
                    ask = j
                    flg = False
                    break
            if flg:
                ask = 1001

            flg = True
            for j in reversed(range(len(buying))):
                if buying[j] != 0:
                    bid = j
                    flg = False
                    break
            if flg:
                bid = 0

            print(str('-' if (ask == 1001) else ask) + ' ' + str('-' if (bid == 0) else bid) + ' ' + str(stock))
            a = 0
