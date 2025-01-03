n = input()
dic = {}
dic['6'] = 0
dic['9'] = 0
for i in n:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
    
cal = dic['6'] + dic['9']
dic['6'], dic['9'] = cal // 2, (cal + 1) // 2

print(max(dic.values()))