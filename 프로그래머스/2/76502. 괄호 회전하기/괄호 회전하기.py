def isOk(string):
    stack = []
    for ch in string:
        if stack and ch == ']' and stack[-1] == '[':
            stack.pop()
        elif stack and ch == '}' and stack[-1] == '{':
            stack.pop()
        elif stack and ch == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(ch)
    if stack:
        return False
    else:
        return True


def solution(s):
    answer = 0
    for i in range(len(s)):
        string = s[i:] + s[0:i] 
        if isOk(string):
            answer += 1
    return answer