from collections import deque
import heapq

def solution(jobs):
    job_count = len(jobs)
    total, time, fta, current_job_index = 0, 0, 0, -1
    
    # 1. 요청 시각 기준 정렬 후 고유 ID 부여
    jobs.sort(key=lambda x: x[0])
    jobs_with_id = [(req, dur, i) for i, (req, dur) in enumerate(jobs)]
    jobs_deque = deque(jobs_with_id)
    
    waiting = []  # 우선순위: (소요시간, 요청시각, 작업번호)

    # 2. 모든 작업이 처리될 때까지 반복
    while jobs_deque or waiting or current_job_index != -1:
        
        # [수정] 해당 시각(time)에 들어온 '모든' 작업을 waiting 큐로 push
        while jobs_deque and jobs_deque[0][0] == time:
            start_time, work_time, jid = jobs_deque.popleft()
            heapq.heappush(waiting, (work_time, start_time, jid))
            
        # 작업 진행 중이면 남은 시간 감소 및 완료 확인
        if current_job_index != -1:
            fta -= 1
            if fta == 0:
                total += (time - jobs[current_job_index][0])
                current_job_index = -1
                
        # 쉬고 있고 대기 작업이 있으면 새 작업 시작
        if current_job_index == -1 and waiting:
            work_time, start_time, jid = heapq.heappop(waiting)
            fta = work_time
            current_job_index = jid
            
        time += 1

    return total // job_count