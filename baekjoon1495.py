'''
DP 기타리스트

'''

import sys
input = sys.stdin.readline
n, s, m = map(int, input().split())
v = list(map(int, input().split()))

res = [[0 for _ in range(m+1)] for _ in range(n+1)]
res[0][s] = 1


for i in range(1, n+1):
    for j in range(m+1):
        if res[i-1][j] == 0:
            continue

        if j + v[i-1] <= m:
            res[i][j+v[i-1]] = 1
        if j - v[i-1] >= 0:
            res[i][j-v[i-1]] = 1

ans = -1

for i in range(m, -1, -1):
    if res[-1][i] == 1:
        ans = i
        break

print(ans)
