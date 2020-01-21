def bfs(x,y) :
    queue = []
    distance = [[0] * m for _ in range(n)]  # 방문 여부 리스트
    dx = [0,0,-1,1] #왼쪽 오른쪽 위 아래
    dy = [-1,1,0,0]

    queue.append((x,y))
    distance[x][y] = 1

    while queue :
        x,y = queue.pop(0)

        for i in range(4) :
            xx, yy = x+dx[i], y+dy[i]
            if xx < 0 or xx >= n : continue
            if yy < 0 or yy >= m : continue 
            if maze[x][y] == 0 : continue
            if distance[xx][yy] != 0: continue

            queue.append((xx,yy))
            distance[xx][yy] = distance[x][y] + 1    # 현 지점까지 거리 표시

    return distance[n-1][m-1]

n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]

print(bfs(0,0))
