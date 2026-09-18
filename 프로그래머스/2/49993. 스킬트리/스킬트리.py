def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        # 선행 스킬 순서에 포함된 문자만 순서대로 추출
        filtered_skills = "".join([s for s in tree if s in skill])
        
        # 추출한 문자열이 선행 스킬트리의 시작 부분과 일치하는지 확인
        if skill.startswith(filtered_skills):
            answer += 1
            
    return answer