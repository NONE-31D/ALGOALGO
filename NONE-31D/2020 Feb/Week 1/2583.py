from collections import deque
import sys
input = sys.stdin.readline

# 전체 좌표
map_l = []
cnt = 2

# 첫 줄 입력
M, N, K = map(int, input().split())
map_l = [[0 for _ in range(N)] for _ in range(M)]

# 두번째 줄 ~ 마지막까지 입력 및 좌표 색칠
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            map_l[i][j] = 1


direction = {
    'x' : [-1,1,0,0],
    'y' : [0,0,-1,1]
}

queue = deque()

for y in range(M):
    for x in range(N):
        if map_l[y][x] != 0:
            continue
        queue.append([y,x])
        while queue:
            curr = queue.popleft()
            curr_y = curr[0]
            curr_x = curr[1]
            if map_l[curr_y][curr_x] == 0:
                map_l[curr_y][curr_x] = cnt
                for i in range(4):
                    next_x = curr_x + direction['x'][i]
                    if next_x < 0 or next_x >= N:
                        continue
                    next_y = curr_y + direction['y'][i]
                    if next_y < 0 or next_y >= M:
                        continue
                    queue.append([next_y, next_x])

        cnt += 1
        

ans = [0 for _ in range(cnt)]
for tmp in map_l:
    for val in tmp:
        ans[val] += 1

ans = ans[2:]
ans.sort()

print(cnt - 2)
print(*ans)
