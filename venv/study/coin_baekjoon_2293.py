# 1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000

def solution(n, k):
    coin = []
    for i in range(n):
        coin.append(int(input()))
    coin.sort()

    dp = [0] * (k+1)
    dp[0] = 1

    for i in coin:
        for j in range(i, k+1):
            dp[j] += dp[j-i]
    print(dp[k])


a = input()
n = int(a.split()[0])
k = int(a.split()[1])
solution(n, k)
