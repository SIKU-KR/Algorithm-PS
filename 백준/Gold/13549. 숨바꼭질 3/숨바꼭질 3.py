from collections import deque

N, K = map(int, input().split())

dp = [float('inf')] * 100001
dq = deque()

dp[N] = 0
dq.append(N)

while dq:
    t = dq.popleft()
    
    if t == K:
        break
    
    if t*2 < 100001 and dp[t] < dp[t*2]:
        dp[t*2] = dp[t]
        dq.appendleft(t*2)
    
    for next_pos in [t-1, t+1]:
        if 0 <= next_pos < 100001 and dp[t] + 1 < dp[next_pos]:
            dp[next_pos] = dp[t] + 1
            dq.append(next_pos)

print(dp[K])