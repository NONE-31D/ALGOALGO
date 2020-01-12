fix_cost, var_cost, labtop = input().split()
fix_cost = int(fix_cost)
var_cost = int(var_cost)
labtop = int(labtop)

# 손익분기점 수식을 생각해보면
# A + B*x < C*x
# A/(C-B) < x
# 그래서 이 수식을 바로 계산해야 함. 21억이 최대치기 때문에 무한루프를 돌면
# 시간초과는 덤이고 오버플로까지 나오는 기염이 터짐
# 수학을 생활화합시다

# 파이썬 // 연산자 : 몫 -> 즉 무조건 버림. 이익이 나기 위해서는 +1
# 생각할거 하나 더 : 아무리 판매 비용이 커도 판매 비용이 가변비용보다
# 작거나 같으면 고정비용에 대한 이득을 취할 수 없음
# 즉 C <= B 일 경우 -1 리턴

if labtop <= var_cost:
    print(-1)
else:
    print(fix_cost//(labtop-var_cost)+1)
