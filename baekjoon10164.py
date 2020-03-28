'''
백준 10164 격자상의 경로

1. 거쳐야 하는 위치의 좌표를 먼저 구하자.

'''

a, b, p = map(int, input().split())

st = [0,0]
if p % b == 0:
    st[0] = b
else:
    st[0] = p % b

dp = [[0]*(b+1) for _ in range(a+1)]


if p % b == 0:
    st[1] = p//b
else:
    st[1] = p//b+1

dp[1][1] = 1

for i in range(1, a+1):
    for s in range(1, b+1):
        if i == 1 and s == 1:
            continue

        if p != 0 and ((i < st[1] and s > st[0]) or ( i > st[1] and s < st[0])):
            dp[i][s] = 0
        else:
            dp[i][s] = dp[i-1][s] + dp[i][s-1]


print(dp[a][b])




