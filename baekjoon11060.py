'''
https://www.acmicpc.net/problem/11060
백준 11060 점프점프

간단한 DP문제.

'''

a = int(input())
jump = list(map(int, input().split()))
jump = [0] + jump

dp = [0] * (a*2)
dp[1] = 1

for i in range(1, a):
    if dp[i] == 0:
        continue

    for j in range(1, jump[i]+1):
        if dp[i+j] > dp[i]+1 or dp[i+j]==0:
            dp[i+j] = dp[i]+1

if dp[a] == 0:
    print(-1)
else:
    print(dp[a] - 1)

