def bfs(x, y) :
    queue = []
    dx = [0,0,-1,1] #왼쪽 오른쪽 위 아래
    dy = [-1,1,0,0]

    queue.append((x,y))
    visited[x][y] = True

    while queue :
        x,y = queue.pop(0)

        for i in range(4) :
            xx, yy = x+dx[i], y+dy[i]
            if xx < 0 or xx >= n : continue
            if yy < 0 or yy >= m : continue 
            if land[xx][yy] == 0 : continue
            if visited[xx][yy] : continue

            queue.append((xx,yy))
            visited[xx][yy] = True


t = int(input())

for _ in range(t) :
    answer = 0
    n, m, k = map(int, input().split())
    land = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]  # 방문 여부 리스트

    for _ in range(k) :
        x, y = map(int, input().split())
        land[x][y] = 1
    
    for i in range(n) :
        for j in range(m) :
            if land[i][j] == 0 : continue
            if visited[i][j] : continue
            bfs(i, j)
            answer = answer + 1
    print(answer)
