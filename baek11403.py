'''
백준 11403 경로찾기
이 문제는 플로이드와샬로 푸는 문제이지만,
파이썬에서 플로이드와샬은 시간초과가 자주 일어난다.

그래서 bfs를 돌리면서
위치에서 다른 위치로의 로써 경로가 있는지 없는지 판단해서 풀면 된다.

ㅁ. 플로이드 와샬이란.
다익스트라 알고리즘을 응용 -> 모든 정점에서 모든 정점으로의 최단거리를 구하는 알고리즘
기본적으로 DP를 바탕으로 함.
최대값 or 최소값을 찾아나가는 것
다익스트라의 가중치 + 최단 경로를 함해서 결과값을 도출

'''


from _collections import deque


def bfs(matrix, n, i):
    visited = [0] * n
    q = deque()
    q.append(i)
    while q:
        idx = q.popleft()
        for i, v in enumerate(matrix[idx]):
            if visited[i] == 0 and v == 1:
                visited[i] = 1
                q.append(i)
    return visited

n = int(input())
matrix = list()
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)


for i in range(n):
    res = bfs(matrix, n, i)
    for s in range(n):
        print(res[s], end =' ')
    print()