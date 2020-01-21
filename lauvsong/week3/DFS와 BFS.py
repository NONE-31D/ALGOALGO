def dfs(start) :
    answer = []
    stack = []
    visited = [False for _ in range(n+1)]  # 방문 여부 리스트

    stack.append(start)
    answer.append(start)
    visited[start] = True

    while stack :
        start = stack[-1]
        deepest = True

        for node in nearby[start] :
            if not visited[node] :
                stack.append(node)
                answer.append(node)
                visited[node] = True
                deepest = False
                break
        if deepest :    # 가장 깊은 노드일 경우
            stack.pop()
    return answer

def bfs(start) :
    answer = []
    queue = []
    visited = [False for _ in range(n+1)]  # 방문 여부 리스트

    queue.append(start)
    answer.append(start)
    visited[start] = True

    while queue :
        start = queue.pop(0)
        
        for node in nearby[start] : 
            if not visited[node] :
                queue.append(node)
                answer.append(node)
                visited[node] = True

    return answer

n,m,v = map(int, input().split())   # 정점, 간선, 탐색 시작 번호
nearby = [ [] for _ in range(n+1) ]  # 인접 리스트

for i in range(m) :    # 인접한 노드들을 각 노드의 배열에 저장해둠
    tmp1, tmp2 = map(int, input().split())
    nearby[tmp1].append(tmp2)
    nearby[tmp2].append(tmp1)

for nodes in nearby :
    nodes.sort()

print(*dfs(v))  # 출력 형태에 맞게 리스트를 풀어주기 위해 * 붙
print(*bfs(v))

