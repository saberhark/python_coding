def solution(N, number):
    answer = 0
    if N==number: return 1
    dp = [set() for _ in range(9)]

    tmp1 = 0
    for i in range(1,9):
        dp[i].add(tmp1*10+N)
        tmp1 = tmp1*10+N

    for i in range(2,9):
        for i in range(1,8):
            for j in range(1,9-i):
                for itmI in dp[i]:
                    for itmJ in dp[j]:
                        dp[i + j].add(itmI + itmJ)
                        dp[i + j].add(itmI * itmJ)
                        if itmI - itmJ > 0:
                            dp[i + j].add(itmI - itmJ)
                        if itmI // itmJ > 0:
                            dp[i + j].add(itmI // itmJ)
        for s in dp:
            if number in s:
                return dp.index(s)
    return -1

a=solution(8, 5800)
print(a)