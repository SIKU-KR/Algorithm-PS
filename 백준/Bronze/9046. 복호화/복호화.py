n = int(input())
for i in range(n):
    d = dict()
    string = input()
    for j in string:
        if j == ' ':
            continue
        elif j in d.keys():
            d[j] += 1
        else:
            d[j] = 1
    max_val = max(d.values())
    max_keys = [k for k, v in d.items() if v == max_val]
    if len(max_keys) == 1:
        print(max_keys[0])
    else:
        print('?')