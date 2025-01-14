def solution(citations):
    answer = 0
    sorted_lst = sorted(citations,reverse=True)
    for i in range(len(citations)):
        if sorted_lst[i] < i+1:
            answer = i
            return answer
    return answer