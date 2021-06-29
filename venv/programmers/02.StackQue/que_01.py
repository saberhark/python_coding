#using que
def solution(progresses, speeds):
    answer = []
    cnt = 0
    day = 0
    while progresses != []:
        while progresses[0] + speeds[0] * day >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            if progresses == []:
                break
        if cnt != 0:
            answer.append(cnt)
            cnt = 0
        day += 1
    return answer

progresses = [93,30,55]
speeds = [1,30,5]
print(solution(progresses, speeds))

# progress [95, 99, 90, 86 ...]
# speed [1,2,1,1 ...]
# return