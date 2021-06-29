def solution(n, lost, reserve):
    answer = 0
    total = [1 for i in range(n+2)]
    total[0] = 0
    total[n+1] = 0
    cnt = 0

    for i in lost:
        total[i] -= 1
    for i in reserve:
        total[i] += 1

    for i in range(1,n+1):
        if total[i] == 0:
            if total[i-1] == 2:
                total[i-1] -= 1
                total[i] += 1
                cnt += 1
            elif total[i+1] == 2:
                total[i+1] -= 1
                total[i] += 1
                cnt += 1
        elif (total[i] == 1) | (total[i] == 2):
            cnt += 1
        answer = cnt
    print(total)
    return answer


a = solution(10,[1,2,3,4,10],[3,4,9])
print(a)