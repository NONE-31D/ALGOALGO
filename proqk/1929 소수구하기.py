n=1000000
#sosu = [i for i in range(0, n+3)]
sosu = [False, False] + [True]*(n+3)
#res=[]

for i in range(2, n+2):
    if sosu[i]:
#       res.append(i)
        for j in range(i*2, n+2, i):
            sosu[j]=False
 
a,b = input().split()
a=int(a)
b=int(b)
#print(res[res.index(a):res.index(b)])
for i in range(a, b+1):
    if sosu[i]:
        print(i)
