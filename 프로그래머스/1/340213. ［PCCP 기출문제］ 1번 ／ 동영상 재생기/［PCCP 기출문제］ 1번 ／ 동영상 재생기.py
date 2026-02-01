def to_seconds(time_str):
    m, s = map(int, time_str.split(':'))
    return m * 60 + s

def to_str(seconds):
    m = seconds // 60
    s = seconds % 60
    return f"{m:02d}:{s:02d}"

def check_opening(current, op_start, op_end):
    # 모두 '초' 단위로 변환해서 비교
    if op_start <= current <= op_end:
        return op_end
    return current

def solution(video_len, pos, op_start, op_end, commands):
    # 1. 모든 입력을 초(seconds)로 변환
    curr = to_seconds(pos)
    v_len = to_seconds(video_len)
    o_start = to_seconds(op_start)
    o_end = to_seconds(op_end)
    
    # 2. 시작하자마자 오프닝 구간인지 체크 (문제 조건에 따라 필요)
    if o_start <= curr <= o_end:
        curr = o_end

    # 3. 명령어 처리
    for cmd in commands:
        if cmd == "prev":
            curr = max(0, curr - 10)  # 0초보다 작아질 수 없음
        elif cmd == "next":
            curr = min(v_len, curr + 10) # 영상 길이보다 길어질 수 없음
            
        # 이동 후 매번 오프닝 구간 체크
        if o_start <= curr <= o_end:
            curr = o_end
            
    # 4. 다시 문자열 포맷으로 변환
    return to_str(curr)