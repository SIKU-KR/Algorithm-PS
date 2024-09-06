string = input()

myList = string.split('-')
# 각 항목을 처리하여 합계를 myList에 반영
for idx in range(len(myList)):
    tmp = myList[idx].split('+')
    sum_val = 0
    for j in tmp:
        sum_val += int(j)
    myList[idx] = sum_val 
# 빼기 계산
ans = int(myList[0])
for i in range(1, len(myList)):
    ans -= myList[i] 

print(ans)
