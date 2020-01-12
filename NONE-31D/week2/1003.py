def fibo(n):
    zero = [1,0]
    one = [0,1]
    if n <= 1:
        return
    
    for i in range(2, n+1):
        zero.append(zero[i-1]+zero[i-2])
        one.append(one[i-1]+one[i-2])
    
    return zero, one

testcase = int(input())
zero_c, one_c = fibo(40)

for _ in range(testcase):    
    n = int(input())
    print(zero_c[n], one_c[n])
    