import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y) :
    cnt = 0
    q = deque()
    q.append((x,y))
    visited = [[False]*n for _ in range(m)] 

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    while q :
        x, y = q.popleft()
        cnt += 1
        visited[x][y] = True

        for i in range(4) :
            xx, yy = x+dx[i], y+dy[i]

            if xx < 0 or xx >= m : continue
            if yy < 0 or yy >= n : continue
            if graph[xx][yy] != 0 : continue
            if visited[xx][yy] : continue

            q.append((xx,yy))
            graph[xx][yy] = 1

    return cnt

m,n,k = map(int,input().split())
graph = [[0]*n for _ in range(m)]
result = []
cnt = 0

for _ in range(k) :
    lx,ly,rx,ry = map(int,input().split())

    for x in range(ly, ry) :
        for y in range(lx, rx) :
           graph[x][y] = 1

for i in range(m) :
    for j in range(n) :
        if graph[i][j] == 0 :
            cnt += 1
            result.append(bfs(i, j))

print(cnt)
print(*sorted(result))
