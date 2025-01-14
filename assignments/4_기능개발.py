# programmers > 스택 / 큐 > 기능개발 
import math
def solution(progresses, speeds):
    answer = []
    left_days = []
    for i in range(len(progresses)):
        left_days.append(math.ceil((100 - progresses[i])/speeds[i]))
    while left_days:
        cur = left_days.pop(0)
        cnt = 1
        while left_days and cur >= left_days[0]:
            left_days.pop(0)
            cnt += 1
        answer.append(cnt)
    return answer