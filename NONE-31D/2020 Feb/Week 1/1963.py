from collections import deque
import sys
input = sys.stdin.readline

# 1이면 합성수 0이면 소수
def is_prime(N):
    global prime_dict

    prime_dict = {
        i : 0 for i in range(N+1)
    }
    prime_dict[0] = 1
    prime_dict[1] = 1
    
    for i in range(2, N+1):
        if i*i >= N:
            break
        if prime_dict[i] == 1:
            continue
        else:
            prime_dict[i] = 0
        for j in range(i+i, N+1, i):
            prime_dict[j] = 1

def transform(first, last):
    visit = {
        k : 0 for k in prime_dict
    }
    cnt = {
        k : -1 for k in prime_dict
    }

    queue = deque()
    queue.append(first)
    cnt[int(first)] = 0
    while queue:
        before = queue.popleft()
        if before == last:
            continue
        
        tmp = visit[int(before)]
        if tmp == 0:
            visit[int(before)] = 1
            for i, _ in enumerate(before):
                for change in range(0,10):
                    after = before
                    after = after[:i]+str(change)+after[i+1:]
                    after = int(after)

                    if prime_dict[after] == 0 and after >= 1000:
                        if cnt[after] == -1 or cnt[after] > cnt[int(before)] + 1:
                            # 처음 방문했거나 최소 거리를 찾았다면
                            cnt[after] = cnt[int(before)] + 1
                        queue.append(str(after))

    return(cnt[int(last)])





is_prime(9999)

K = int(input())
for _ in range(K):
    first, last = map(str, input().split())
    ans = transform(first, last)
    if ans == -1:
        ans = "Impossible"
    print(ans)




