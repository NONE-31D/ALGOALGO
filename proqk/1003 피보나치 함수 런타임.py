dp0={0:1, 1:0}

dp1={0:0, 1:1}

 

T = int(input())

while T>0 :

    N = int(input())

 

    for i in range(2, 40, 1) :

        dp0[i] = dp0[i-2]+dp0[i-1]

        dp1[i] = dp1[i-2]+dp1[i-1]

    

    print(dp0[N], dp1[N])

    T-=1
