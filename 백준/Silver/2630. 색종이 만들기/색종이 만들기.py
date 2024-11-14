def is_all_element_n(target, n):
    for i in target:
        for j in i:
            if j != n:
                return False
    return True

def div_and_conquer(target, size):
    global blue
    global white
    if size == 1:  # 크기가 1인 경우 처리
        if target[0][0] == 1:
            blue += 1
        elif target[0][0] == 0:
            white += 1
        return
    
    if is_all_element_n(target, 1):  # 모든 요소가 1인지 확인
        blue += 1
        return
    elif is_all_element_n(target, 0):  # 모든 요소가 0인지 확인
        white += 1
        return
    
    # 사분할로 나누기
    half = size // 2
    div_and_conquer([row[:half] for row in target[:half]], half)       # 왼쪽 위
    div_and_conquer([row[half:] for row in target[:half]], half)       # 오른쪽 위
    div_and_conquer([row[:half] for row in target[half:]], half)       # 왼쪽 아래
    div_and_conquer([row[half:] for row in target[half:]], half)       # 오른쪽 아래

blue = 0
white = 0
N = int(input())
li = []
for i in range(N):
    inp = list(map(int, input().split()))
    li.append(inp)
div_and_conquer(li, N)
print(white)
print(blue)