from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * (bridge_length - 1))
    truck_weights = deque(truck_weights)
    now_sum = sum(bridge)

    while True:
        if not truck_weights:
            break
        if now_sum + truck_weights[0] <= weight:
            bridge.append(truck_weights.popleft())
            now_sum += bridge[-1]
        else:
            bridge.append(0)
        now_sum -= bridge.popleft()
        answer += 1

    return answer + bridge_length
