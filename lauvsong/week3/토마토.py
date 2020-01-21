from collections import deque # 시간 초과 안 뜨려면 deque 로 

def bfs(box, n, m) :
    dx = [0,0,-1,1] #왼쪽 오른쪽 위 아래
    dy = [-1,1,0,0]
    day = -1

    while queue :
        day = day + 1
        for _ in range(len(queue)) :
            x,y = queue.popleft()

            for i in range(4) :
                xx, yy = x+dx[i], y+dy[i]

                if xx < 0 or xx >= n : continue
                if yy < 0 or yy >= m : continue
                if box[xx][yy] != 0 : continue

                box[xx][yy] = 1
                queue.append((xx, yy))

    for tomato in box :
        if 0 in tomato :
            return -1
    return day


m,n = map(int, input().split())
box = []
queue = deque()

for i in range(n) :
    line = list(map(int, input().split()))
    for j in range(m) :
        if line[j] == 1 :
            queue.append((i,j))
    box.append(line)

print(bfs(box,n,m))
        
