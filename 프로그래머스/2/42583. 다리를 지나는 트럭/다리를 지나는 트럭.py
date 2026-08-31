from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque([0] * (bridge_length - 1)) 
    waiting = deque(truck_weights)
    current_weight = 0
    
    while (bridge or waiting):
        answer += 1
                    
        # deque
        if len(bridge) == bridge_length:
            done = bridge.popleft()
            current_weight -= done
        elif not waiting:
            bridge.popleft()
        
        # enque
        if waiting and len(bridge) < bridge_length and current_weight + waiting[0] <= weight:
            next_truck = waiting.popleft()
            bridge.append(next_truck)
            current_weight += next_truck 
        elif waiting:
            bridge.append(0)
        
        # print(answer, bridge, waiting)
    
    return answer