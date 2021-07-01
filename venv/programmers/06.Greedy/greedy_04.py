def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    #while people !=[]:
    length = len(people)
    back = 0

    for i in range(length):
        if (people[length - 1 - back] * 2 > limit) | (length-1-back-i <=0):
            answer += length - i -back
            return answer

        if (people[i] * 2 <= limit) :
            answer += int((length-i-back)/2) if (length-i-back)%2 == 0 else int((length-i-back+1)/2)
            return  answer

        if people[i]+people[length-1-back] <= limit:
            back += 1
        answer += 1
    return answer

#people = [70, 50, 80, 50]
#people = [70, 50, 80]
people = [10,20,30,40,50,60,70,80,90]
limit = 100
a = solution(people,limit)
print(a)