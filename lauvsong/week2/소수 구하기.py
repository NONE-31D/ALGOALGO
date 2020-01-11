/* 에라토스테네스의 체 */
mini,maxi = map(int,input().split())
a=[0,0]+[int(i) for i in range(2,maxi+1)]

for i in range(2,maxi+1) :
    if a[i]!=0 :
        for j in range(2*i,maxi+1,i) :
            a[j]=0
            
a=sorted(list(set(a[mini:]))) // mini보다 큰 인덱스 값들 중복 제거 및 정렬
a.remove(0) // 0 제거
for num in a :
    print(num)
    
