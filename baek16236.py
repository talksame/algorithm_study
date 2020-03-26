'''
백준 16236 아기상어


풀이 조건
1. 상어는 자신이 먹을 수 있는 물고기가 없을 때 종료.
2. 상어는 가장 가까운 물고기 > 가장 위에 있는 > 가장 왼쪽에 있는 물고기를 우선 챙김
3. if 물고기가 1마리라면 그 물고기를 먹고 프로그램 종료함.

기본 조건
상어의 최초 크기는 2
물고기는 1~6
상어의 위치는 9

풀이과정
1. 일단 물고기를 다 먹고, 먹은 물고기들을 정리해서 이동거리를 파악하자.

오류가 있어서 새롭게 폴기로 함.
heapq 사용.

기타.
삼성 입사 시험에 나왔던 문제의 응용판 (물고기의 모험)
'''


'''
오류코드
from collections import deque
# v = st
def bfs(v):
    global st, cnt, size, ans

    #큐로 먹은 물고기들 구하기.
    q = deque()
    visit = [[0]*n for _ in range(n)]
    q.append(v)
    visit[v[0]][v[1]] = 1
    eat = []
    flag = False
    #다음 물고기까지의 거리
    distance = 0

    while q:
        distance += 1
        x, y = q.popleft()
        for s in range(4):
            nx = x + dx[s]
            ny = y + dy[s]
            if 0 <= nx < n - 1 and 0 <= ny < n - 1 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if matrix[nx][ny] == 0 or matrix[nx][ny] == size:
                    q.append([nx, ny])
                elif 0 < matrix[nx][ny] < size:
                    eat.append([nx, ny])
                    flag = True
    #먹은 물고기들의 거리 값 알아내기
    if flag:
        eat.sort(key = lambda x: [x[0], x[1]])
        matrix[eat[0][0]][eat[0][1]] = 9
        matrix[st[0]][st[1]] = 0
        st = eat[0]
        cnt += 1
        print(ans)
        ans += distance

        if cnt == size:
            size += 1
            cnt = 0
    else:
        pass
    return flag

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
matrix = list()
cnt = 0
size = 2
ans = 0
st = 0
for i in range(n):
    temp = list(map(int, input().split()))
    matrix.append(temp)
    for a, b in enumerate(temp):
        if b == 9:
            st = [i, a]

for i in range(n):
    print(matrix[i])

while True:
    temp = bfs(st)
    if temp == False:
        break
print(ans)


'''

'''
heapq를 사용해서 풀기.


너무 어렵게 풀었당.
결국 상어와 물고기 크기가 같아지는 지점을 고려하면 된다.
+ 가장 가까운 경우도 고려.


'''
from heapq import heappush, heappop

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
q = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            #시작 위치를 heapq에 넣기 <- 위의 코드에서 졍렬과정을 제거 한 것.
            heappush(q, (0, i, j))
            matrix[i][j] = 0

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

def bfs():
    global q
    size = 2
    eat = 0
    distance = 0
    visit = [[0] * n for _ in range(n)]
    while q:
        d, y, x = heappop(q)
        if 0 < matrix[y][x] < size:
            eat += 1
            matrix[y][x] = 0
            if eat == size:
                size += 1
                eat = 0
            distance += d
            d = 0
            q = []
            visit = [[0]*n for _ in range(n)]
        for a in range(4):
            nd = d+1
            ny = y + dy[a]
            nx = x + dx[a]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if 0 < matrix[ny][nx] > size or visit[ny][nx]:
                continue
            visit[ny][nx] = 1
            heappush(q, (nd, ny, nx))
    print(distance)

bfs()


