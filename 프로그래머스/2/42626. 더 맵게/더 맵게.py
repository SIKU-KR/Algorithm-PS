import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        a = heapq.heappop(scoville)
        
        # end condition
        if a >= K:
            return answer
        if len(scoville) == 0:
            return -1
        
        # mix foods
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + (b*2))
        answer += 1
    