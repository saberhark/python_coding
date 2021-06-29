def solution(clothes):
    answer = 1
    dic = {}
    for arr in clothes:
        dic[arr[1]] = dic.get(arr[1], 0) + 1
    for value in dic.values():
        answer *= value+1
    return answer-1


from functools import reduce


def lambda_solution(clothes):
    dic = {}
    for arr in clothes:
        dic[arr[1]] = dic.get(arr[1], 0) + 1
    return reduce(lambda x, y: x*(y+1), dic.values(), 1)-1


from collections import Counter


def counter_solution(clothes):
    # dic = Counter([kind for name, kind in clothes])
    dic = Counter([arr[1] for arr in clothes])
    return reduce(lambda x, y: x*(y+1), dic.values(), 1)-1


#시발
def oneline_solution(clothes):
    return reduce(lambda x, y: x*(y+1), Counter([arr[1] for arr in clothes]).values(), 1)-1



ans = counter_solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"],["yellowhat", "cap"]])
ans2 = lambda_solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"],["yellowhat", "cap"]])

print(ans)
print(ans2)
