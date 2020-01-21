def bfs(start) :
    answer = 0
    queue = []
    visited = [False for _ in range(computers+1)]  # 방문 여부 리스트

    queue.append(start)
    visited[start] = True

    while queue :    # 큐가 비면 1번과 이어져있는 그래프는 모두 센것
        start = queue.pop(0)
        
        for node in nearby[start] : 
            if not visited[node] :
                queue.append(node)
                answer = answer + 1
                visited[node] = True

    return answer

computers = int(input())
pairs = int(input())

nearby = [[] for _ in range (computers+1)]

for i in range(pairs) :    # 인접 리스트
    tmp1, tmp2 = map(int, input().split())
    nearby[tmp1].append(tmp2)
    nearby[tmp2].append(tmp1)

print(bfs(1))
