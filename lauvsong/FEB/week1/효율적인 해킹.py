import sys
from collections import deque

def bfs(linked, start) :
    count = 0
    q = deque()
    q.append(start)
    visited = [False for _ in range(n+1)] 
    visited[start] = True
    while q :
        popped = q.popleft()
        count += 1

        for node in linked[popped] :
            if not visited[node] :
                q.append(node)
                visited[node] = True

    return count

input = sys.stdin.readline

n,m = map(int,input().split())
linked = [[] for _ in range(n+1)]
result = []

for i in range(m) :
    a, b = map(int,input().split())
    linked[b].append(a)

maxi = 0
for i in range(1, n+1) :
    if linked[i] :
        value = bfs(linked, i)
        if maxi <= value :
            if maxi < value : 
                maxi = value
                result = []
            result.append(i)

print(*result)
