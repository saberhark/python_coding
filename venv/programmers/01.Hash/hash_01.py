def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]


ans = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])

print(ans)


######### using Dictionary #######

def dic_solution(participant, completion):
    answer = ''
    dic = {}
    for part in participant:
        dic[part] = dic.get(part, 0)+1
    for comp in completion:
        if dic[comp]-1 == 0:
            del(dic[comp])
        else:
            dic[comp] -= 1
    answer = dic.keys()

    for answer in list(answer):
        answer = answer
    return answer


print(dic_solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
