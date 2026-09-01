# bfs해서 unvisited count - visited count 반환
def bfs(n, graph):
    visited = [False] * n
    stk = []
    stk.append(0)
    visited[0] = True
    while stk:
        p = stk.pop()
        for i in graph[p]:
            if not visited[i]:
                stk.append(i)
                visited[i] = True
    return abs(visited.count(True) - visited.count(False))


# 2차원 배열로 양방향 그래프 만들어서 반환
def create_graph(n, wires):
    graph = [ [] for _ in range(n) ]
    for fr, to in wires:
        graph[fr-1].append(to-1)
        graph[to-1].append(fr-1)
    return graph


# 그래프만들어서 bfs 돌리고 최소값 보관 
def solution(n, wires):
    answer = []
    for i in range(len(wires)):
        new_wires = wires[:i] + wires[i+1:]
        graph = create_graph(n, new_wires)
        a = bfs(n, graph)
        answer.append(a)
    print(answer)
    return min(answer)