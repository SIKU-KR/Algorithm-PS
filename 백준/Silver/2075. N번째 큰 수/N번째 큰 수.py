def find_max_index(li):
    max_number = max(li)
    max_index = li.index(max_number)
    return max_number, max_index

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
graph.reverse()

now = 0
current = graph[0]
idx = {}
for i in range(n):
    idx[i] = 0

for i in range(n):
    max_num, max_idx = find_max_index(current)
    if idx[max_idx] + 1 < n:
        current[max_idx] = graph[idx[max_idx] + 1][max_idx]
        idx[max_idx] += 1
    else:
        current[max_idx] = -999999
    now = max_num

print(now)
