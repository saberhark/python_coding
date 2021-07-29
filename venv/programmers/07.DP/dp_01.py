def solution(N, number):
    answer = 0
    if N==number: return 1
    dp = [set() for _ in range(9)]

    tmp1 = 0
    for i in range(1,9):
        dp[i].add(tmp1*10+N)
        tmp1 = tmp1*10+N

    for i in range(2,9):
        for j in range(1, 1+i//2):
            for itm1 in dp[j]:
                for itm2 in dp[i-j]:
                    dp[i].add(itm1 + itm2)
                    dp[i].add(itm1 * itm2)

                    if max(itm1 - itm2, itm2 - itm1) > 0:
                        dp[i].add(max(itm1 - itm2, itm2 - itm1))

                    if max(itm1 // itm2, itm2 // itm1) > 0:
                        dp[i].add(max(itm1 // itm2, itm2 // itm1))

    """"
    for i in range(1,8):
        for j in range(1,9-i): # i~ 9-i로 순회하면 안된다 > 5 = 1+4 인데 4는 미완성이기 떄문 (1+3만 들어 있고 2+2가 안들어 있는 상태)
            print(i,j)
            for itmI in dp[i]:
                for itmJ in dp[j]:
                    dp[i + j].add(itmI + itmJ)
                    dp[i + j].add(itmI * itmJ)

                    if max(itmI - itmJ, itmJ - itmI) > 0:
                        dp[i + j].add(max(itmI - itmJ, itmJ - itmI))

                    if max(itmI // itmJ, itmJ // itmI) > 0:
                        dp[i + j].add(max(itmI // itmJ, itmJ // itmI))
    """""

    for s in dp:
        if number in s:
            return dp.index(s)

    return -1


a=solution(8, 5800)
print(a)