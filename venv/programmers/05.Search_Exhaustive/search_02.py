def solution(numbers):
    answer = 0
    arr = [int(i) for i in numbers]
    prime = [1]*(10**len(numbers))

    prime[0] = 0
    prime[1] = 0
    for i in range(2,int(len(prime)**(1/2))):
        if prime[i]==1:
            for i in range(i*2,len(prime), i):
                prime[i]=0
    #for i in range(len(prime)):
    #    print(i,prime[i])

    permutation(0, arr, prime)
    answer=prime.count(2)

    return answer

def permutation(num, arr, prime):
    check(num, prime)
    for _ in arr:
        tmp = arr[0]
        permutation(num*10 + arr.pop(0), arr, prime)
        arr.append(tmp)

def check(num, prime):
    if prime[num]==1:
        prime[num]=2
        return 1
    else:
        return 0

print(solution("17"))