# https://www.acmicpc.net/problem/20546

cash = int(input())
price = list(map(int, input().split()))

def jh():
    global cash, price
    money = cash
    count = 0
    for a in price:
        avail = money // a
        money -= avail * a
        count += avail
    return count * price[-1] + money


def sm():
    global cash, price
    before = price[0]
    rally = 0
    money = cash
    count = 0
    for i in range(1, len(price)):
        if price[i] > before:
            if rally < 0:
                rally = 1
            elif rally >= 0 and rally < 2:
                rally += 1
            elif rally == 2:
                money += count * price[i]
                count = 0
        elif price[i] < before:
            if rally > 0:
                rally = -1
            elif rally <= 0 and rally > -2:
                rally -= 1
            elif rally == -2:
                avail = money // price[i]
                count += avail
                money -= avail * price[i]
        else:
            rally = 0
    return count * price[-1] + money

jhrs = jh()
smrs = sm()
if jhrs > smrs:
    print('BNP')
elif jhrs < smrs:
    print('TIMING')
else:
    print('SAMESAME')
