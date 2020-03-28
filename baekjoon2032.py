'''
https://www.acmicpc.net/problem/2302

백준 2302번 극장 좌석.

'''

chair = int(input())
case = int(input())
dp = [0]*41
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 41):
    dp[i] = dp[i-1]+dp[i-2]
res = list()
for i in range(case):
    res.append(int(input()))

pre = 0
sum = 1
for i in res:
    sum *= dp[i - pre - 1]
    pre = i
sum *= dp[chair - pre]
print(sum)



