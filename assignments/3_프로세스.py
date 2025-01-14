# programmers > 스택 / 큐 > 프로세스  
def solution(priorities, location):
    answer = 0
    task_q = list()
    
    for idx,value in enumerate(priorities):
        task_q.append((idx,value))
    while True: 
        cur = task_q.pop(0)
        if any(cur[1] < task[1] for task in task_q ):
            task_q.append(cur)
        else: 
            answer += 1 
            if cur[0] == location:
                return answer