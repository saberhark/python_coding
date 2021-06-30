# print(max(int(i) for i in number))
# print(max(i for i in number))
# print(max(number))

def solution(number, k):
    answer = ''
    idx = 0

    while k>0:
        tmpIdx = 0
        maxNum = int(number[idx])
        #tmpIdx = number[idx: idx+k+1].index(max(number[idx: idx+k+1]))
        for i in range(k+1):
            if int(number[idx+i]) > maxNum:
                maxNum = int(number[idx+i])
                tmpIdx = i
            if maxNum == 9:
                break

        answer += number[idx+tmpIdx]
        idx += tmpIdx+1
        k -= tmpIdx
        if len(number)-idx-1 < k:
            return answer

    answer += number[idx:]
    return answer

a = solution("1111117",5)
print(a)