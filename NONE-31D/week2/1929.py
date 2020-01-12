# 소수찾기는 에라스토테네스가 제일 나은...가? 모든 소수 찾기엔 얘가 그나마 빠른 편

# 파이썬으로 스페이스 포함 입력받는 방법. map으로 자료형까지 변환 가능
m, n = map(int, input().split())

# 0: 합성수
# 1: 약수

prime = [True]*(n+1)
prime[0] = False
prime[1] = False
end = int(n ** 0.5)

for i in range(2, end+1):
    if prime[i]:
        for j in range(i+i, n+1, i):
            prime[j] = False
            
for idx, isPrime in enumerate(prime):
    if idx < m:
        continue
    if isPrime:
        print(idx)