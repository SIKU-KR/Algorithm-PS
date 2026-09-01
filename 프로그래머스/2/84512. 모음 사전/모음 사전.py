def solution(word):
    vowels = ['U', 'O', 'I', 'E', 'A']  # 'A'가 가장 늦게 들어가서 가장 먼저 pop되도록 역순 정의
    stack = [""]
    count = 0
    
    while stack:
        current = stack.pop()
        
        # 빈 문자열(시작점)이 아닌 경우 카운트 증가
        if current:
            count += 1
            if current == word:
                return count
        
        # 길이가 5 미만일 때만 다음 글자를 붙여서 스택에 추가
        if len(current) < 5:
            for v in vowels:
                stack.append(current + v)

    return count