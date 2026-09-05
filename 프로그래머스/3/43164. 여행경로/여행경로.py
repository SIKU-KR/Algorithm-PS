def solution(tickets):
    # 사전순으로 정렬 (가장 먼저 완성된 경로가 사전순으로 가장 앞섬)
    tickets.sort()
    visited = [False] * len(tickets)
    answer = []

    def dfs(current_airport, path):
        # 모든 티켓을 다 사용한 경우 (방문 공항 수는 티켓 수 + 1)
        if len(path) == len(tickets) + 1:
            answer.extend(path)
            return True

        for i, (start, end) in enumerate(tickets):
            if start == current_airport and not visited[i]:
                visited[i] = True
                if dfs(end, path + [end]):
                    return True  # 정답을 찾으면 즉시 탐색 종료
                visited[i] = False  # 막다른 길이면 원상복구(백트래킹)
        
        return False

    dfs("ICN", ["ICN"])
    return answer