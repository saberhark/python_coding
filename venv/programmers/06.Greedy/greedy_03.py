def solution(number, k):
    answer = ''
    a = dict(zip(range(len(number)), [i for i in number]))
    #print(a)

    sorted(a.items(), key=lambda x: x[1], reverse=True)

    for (k,v) in sorted(a.items(), key=lambda x: x[1], reverse=True):


    return answer


a = solution("4177252841",4)
print(a)