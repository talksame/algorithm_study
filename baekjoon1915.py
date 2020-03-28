'''
백준 1915 가장 큰 정사각형

DP를 가장한 bfs

풀이 조건
1. 1의 위치를 정하고 그 위치로부터 왼, 아래 대각선 위치가 또 1인지 확인.

2. 모두 1이면 level += 1

3. 그 값들을 큐에 넣고 다시 판단 -> 하나라도 0이면 break

최대값은 level^2

위의 방법은 런타임 오류 DP로 계산해야한다.

점화식
if v[a][b]:
v[a][b] = min(v[a-1][b] + min(v[a][b-1] , v[a-1][b-1]) + 1

for s in range(a):
    for k in range(b):
        matrix[s][k] = int(matrix[s][k])

'''

a, b = map(int, input().split())

matrix = list()
for i in range(a):
    matrix.append(list(input()))
    for k in range(b):
        matrix[i][k] = int(matrix[i][k])

def solution(board):
    for i in range(1,len(board)):
        for j in range(1,len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1],board[i-1][j],board[i][j-1]) + 1
    m=0
    for i in range(len(board)):
        if m < max(board[i]):
            m = max(board[i])
    return m**2

print(solution(matrix))



