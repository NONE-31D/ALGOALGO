import sys
import math
from collections import deque
input = sys.stdin.readline

def bfs(prev,next) :
    q = deque()
    q.append(prev)
    cnt = [0] * 10000
    visited = [False] * 10000 
    visited[prev] = True

    while q :
        curr = q.popleft()
        if (curr == next) : return cnt[next]

        tmp = str(curr)
        for i in range(4) :
            for j in range(10) :
                tmp2 = tmp[0:i] + str(j) + tmp[i+1:]
                result = int(tmp2)
                if visited[result] : continue
                if result < 1000 : continue
                if not isPrime[result] : continue

                visited[result] = True
                q.append(result)
                cnt[result] = cnt[curr] + 1

    return "Impossible"

t = int(input())
isPrime = [False, False] + [True] * 9998

for i in range(2, int(math.sqrt(9999))+1) : 
    if isPrime[i] :
        isPrime[i*2::i] = [False] * len(isPrime[i*2::i])

for i in range(t) :
    a,b = map(int, input().split())
    print(bfs(a,b))
