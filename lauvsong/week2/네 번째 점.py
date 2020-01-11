xx=[]
yy=[]

for i in range(3) :
    tmpx,tmpy = map(int, input().split())
    xx.append(tmpx)
    yy.append(tmpy)

for i in range(3) :
    if xx.count(xx[i]) == 1 : // 1개만 포함되어 있을 시 그 값이 네 번째 좌표임
        x = xx[i]
    if yy.count(yy[i]) == 1 :
        y = yy[i]

print(x,y)
