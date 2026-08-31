import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    for o in operations:
        if o.startswith("I"):
            a = int(o[2:])
            heapq.heappush(max_heap, a * -1)
            heapq.heappush(min_heap, a)
        elif o == "D 1" and max_heap:
            # 최대힙에서 삭제하고, 그 값을 min_heap에서 remove 한 뒤, heapify
            target = heapq.heappop(max_heap) * -1
            min_heap.remove(target)
            heapq.heapify(min_heap)
        elif o == "D -1" and min_heap:
            # 최소힙에서 삭제하고, 그 값을 max_heap에서 remove 한 뒤, heapify
            target = heapq.heappop(min_heap) * -1
            max_heap.remove(target)
            heapq.heapify(max_heap)

    if not max_heap:
        return [0, 0]
            
    max_value = heapq.heappop(max_heap) * -1
    min_value = heapq.heappop(min_heap)
    return [ max_value, min_value ]