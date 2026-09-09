from collections import deque

def solution(order):

    # 목표 : O(N) , N <= 1,000,000
    # 컨테이너 벨트에는 1번박스 - N번박스가 실려있음
    main_belt = deque()
    for i in range(1, len(order)+1):
        main_belt.append(i)
    sub_belt = []
    s = set()
    q = deque(order)
    
    # order의 순서대로 (숫자)번 상자대로 실어야함
    # 보조 컨테이너 벨트는 맨 앞의 상자만 뺄 수 있음 (스택)
    # 메인벨트에서는 어떻게든 꺼내서 실을 수 있는데, 보조벨트에서는 맨앞이 아니면 안됨.
    answer = 0
    
    while q:
        if sub_belt and sub_belt[-1] == q[0]:
            # 찾았다. 스택 팝.
            sub_belt.pop()
            q.popleft()
            answer += 1
        elif main_belt and main_belt[0] == q[0]:
            # 찾았다, 디큐.
            main_belt.popleft()
            q.popleft()
            answer += 1
        elif main_belt and q[0] not in s:
            # 디큐, 집합에 추가, 서브벨트 추가
            i = main_belt.popleft()
            s.add(i)
            sub_belt.append(i)
        elif sub_belt[-1] != q[0] and i in s:
            # 종료조건
            break
            
    return answer