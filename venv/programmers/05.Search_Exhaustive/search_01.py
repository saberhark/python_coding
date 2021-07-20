def solution(answers):
    answer = []
    answers1 = [1, 2, 3, 4, 5]
    answers2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answers3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    (score1,score2,score3) = (0,0,0)

    for i in range(len(answers)):
        score1 += 1 if answers[i]==answers1[i%len(answers1)] else 0
        score2 += 1 if answers[i] == answers2[i % len(answers2)] else 0
        score3 += 1 if answers[i] == answers3[i % len(answers3)] else 0

    m = max(score1,score2,score3)

    if m == score1:
        answer.append(1)
    if m == score2:
        answer.append(2)
    if m == score3:
        answer.append(3)

    return answer


print(solution([1,2,3,4,5]))


# 1, 2, 3, 4, 5, / 1, 2, 3, 4, 5, ...
# 2, 1, 2, 3, 2, 4, 2, 5, / 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, / 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...