def solution(priorities, location):
    answer = 0
    cnt = 0
    max_pri = sorted(priorities, reverse=True)

    while priorities != []:
        if priorities[0] == max_pri[0]:
            priorities.pop(0)
            max_pri.pop(0)
            cnt += 1
            if location == 0:
                answer = cnt
            location -= 1
        else:
            priorities.append(priorities.pop(0))
            location -= 1
            if location < 0:
                location = len(priorities) - 1
    return answer

#priorites = [1,1,9,1,1,1]
#location = 0
priorites = [2,1,3,2]
location = 2

print(solution(priorites, location))