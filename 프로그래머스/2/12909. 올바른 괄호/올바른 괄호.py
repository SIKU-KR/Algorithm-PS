def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
            continue
        elif i == ')':
            try:
                a = stack.pop()
            except Exception:
                return False
    return len(stack) == 0