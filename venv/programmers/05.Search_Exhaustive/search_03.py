def solution(brown, yellow):
    answer = []
    for i in range(1,int((brown+yellow)**(1/2))):
        if (i)*(int(brown/2)-i-2) == yellow:
            answer = [int(brown / 2) - i, i + 2]
            answer.sort(reverse=True)
    return answer

print(solution(24,24))