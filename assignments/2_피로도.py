# programmers - 피로도
## 순열로 노가다 돌기 [o] -> 모든 경우의 수 다 돌아서 그 중에 max값 == answer
## 재귀로 풀어보기 [ ]
## DFS로도 푸는 법 공부 하기 [ ]
import itertools
def solution(k, dungeons):
    nPr = itertools.permutations(dungeons, len(dungeons))
    order_list = list(nPr)
    life = k
    max_explored = -1

    for i in order_list:
        current_life = life
        num_of_explore = 0
        for min_required, cost in i:
            if min_required <= current_life: #대소 조건에서 실수 많음,, 잘 보기 
                current_life -= cost
                num_of_explore += 1
            else:
                break
        if max_explored < num_of_explore:
            max_explored = num_of_explore

    answer = max_explored
    return answer