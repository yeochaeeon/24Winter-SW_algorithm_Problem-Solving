# programmers - H-index
def solution(citations):
    answer = 0
    iter = 0
    cnt = 0
    citations.sort()
    for i in range(max(citations)+1):
        iter = i
        cnt = 0
        for j in range(len(citations)):
            if iter <= citations[j] :
                cnt+=1
        # print(iter,cnt)
        if iter <= cnt :
            answer = i
    return answer


print(solution([4,4,4])) # 3
print(solution([3, 0, 6, 1, 5])) # 3