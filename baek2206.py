'''
백준 2206 벽 부수고 최단경로

기초문제는 아닌 듯.
heapq + 3차원 배열로 연산시 한 번에 2개씩 연산해야함.

풀이 조건
1. 벽을 1개 부슨다 = 벽이 안 부셔진 경우, 벽을 부술 수 있는 경우를 모두 고려

기본 조건
1, 1 -> n, m까지 이동
벽 위치를 띄어쓰기 없는 문자열로 준다.


풀이과정
1. heapq 가 필요하다. cnt가 가장 낮은 경우를 찾아야 하기 때문에
결국 이 문제도 bfs보다는 다익스트라 알고리즘에 가깝다.

2. 차원을 2개 구해줘야 한다. 벽을 깨는 경우와 벽을 깨지 않는 경우가 있기 때문이다.
이를 표현하기 위해서 matrix[x][y][z] / z = 1 or 0 로 구분한다.

'''

import sys
from collections import deque
import heapq

def sol():
    q = []
    heapq.heappush(q, [1, 0, 0, 0])
    visit[0][0][0] = 1
    while q:
        #cnt는 횟수 x,y 좌표 c는 1을 지우지 않은 경우.
        cnt, x, y, c = heapq.heappop(q)
        #목적지 도착시 종료.
        if x == n - 1 and y == m - 1:
            return cnt

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny][c] == 0:
                visit[nx][ny][c] = 1
                if matrix[nx][ny] == '0':
                    heapq.heappush(q, [cnt+1, nx, ny, c])
                if matrix[nx][ny] == '1' and c == 0:
                    heapq.heappush(q, [cnt + 1, nx, ny, 1])
    #q가 끝나도 목적지에 도착을 못하면 -1을 출력
    return -1


n, m = map(int, input().split())
#이제보니 문자열이네요.
matrix = [input() for _ in range(n)]
visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

print(sol())

