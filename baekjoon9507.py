'''
백준 9507 새로운 피보나치

간단한 DP문제
그러나 재귀로 풀면 안됨 -> call error 발생
'''

dp = [0] * 68

dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 68):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]

a = int(input())
res = list()
for i in range(a):
    temp = int(input())
    res.append(dp[temp])

for i in range(a):
    print(res[i])