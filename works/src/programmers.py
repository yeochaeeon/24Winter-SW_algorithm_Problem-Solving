def p42747(citations):
    # https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3
    answer = 0
    citations.sort(reverse=True)
    for i, citation in enumerate(citations, start=1):
        answer = max(answer, min(i, citation))
    return answer


def p87946(k, dungeons):
    # https://school.programmers.co.kr/learn/courses/30/lessons/87946
    from itertools import permutations

    answer = 0
    n = len(dungeons)
    for order in permutations(range(n)):
        current_k = k
        count = 0
        for i in order:
            min_fatigue, consumed_fatigue = dungeons[i]
            if current_k >= min_fatigue:
                current_k -= consumed_fatigue
                count += 1
        answer = max(answer, count)
    return answer


def p12909(s):
    # https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3
    mapping = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in s:
        if char in mapping:
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return not stack


def p42583(bridge_length, weight, truck_weights):
    # https://school.programmers.co.kr/learn/courses/30/lessons/42583
    from collections import deque

    time = 0
    total_weight = 0

    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    while bridge:
        time += 1

        exited_truck = bridge.popleft()
        total_weight -= exited_truck

        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                new_truck = truck_weights.popleft()
                bridge.append(new_truck)
                total_weight += new_truck
            else:
                bridge.append(0)
    return time


def p43165(numbers, target):
    # https://school.programmers.co.kr/learn/courses/30/lessons/43165
    stack = [(0, 0)]  # (현재 인덱스, 현재 합)
    count = 0

    while stack:
        index, current_sum = stack.pop()
        if index == len(numbers):
            if current_sum == target:
                count += 1
        else:
            stack.append((index + 1, current_sum + numbers[index]))
            stack.append((index + 1, current_sum - numbers[index]))
    return count


def p43165_v2(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0
        return dfs(index + 1, current_sum + numbers[index]) + dfs(
            index + 1, current_sum - numbers[index]
        )

    return dfs(0, 0)
