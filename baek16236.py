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
이 코드가 복잡한 이유, 우선순위를 만들어주기 어려웠다.
우선순위를 쉽게 설정할 수 있는 heapq를 사용해야한다.
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

c 언어로 나타내자면, 
struct snake(){
    현재 사이즈
    현재 움직인 거리
    현재 좌표
}이런식으로 모두 가지고 있는 q를 heap 형태로 유지해야함.

heap의 우선순위
거리, ,y좌표, x좌표 순으로 넣어줌.
2. 상어는 가장 가까운 물고기 > 가장 위에 있는 > 가장 왼쪽에 있는 물고기를 우선 챙김



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

#상하좌우를 모두 가봐야 하는 bfs문제.
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

def bfs():
    global q
    #size = 크기, eat = 먹은 물고기의 개수, distance = 움직인 거리
    size = 2
    eat = 0
    distance = 0
    visit = [[0] * n for _ in range(n)]
    while q:
        d, y, x = heappop(q)
        #물고기가 size이하면 먹고, 행여 먹은 물고기의 크기가 size와 동일하다면 크기를 증가시켜준다.
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
            #nd = 움직인 거리는 1칸 움직일 때 마다 증가시켜줌.
            nd = d+1
            ny = y + dy[a]
            nx = x + dx[a]
            # 먹는 경우는 들어올 때 처리하기 때문에, 먹지 못하는 경우를 걸러줌.
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if 0 < matrix[ny][nx] > size or visit[ny][nx]:
                continue
            visit[ny][nx] = 1
            heappush(q, (nd, ny, nx))
    print(distance)

bfs()


