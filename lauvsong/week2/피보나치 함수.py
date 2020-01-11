// 숫자에 따른 0과 1이 호출되는 수 또한 피보나치 수열 관계에 있다는 것을 활용
def getZeroOne(num) :
    length = len(zero)
    if length <= num :
        for i in range(length, num+1) :
             zcount = zero[i-2]+zero[i-1]
             zero.append(zcount)
             ocount = one[i-2]+one[i-1]
             one.append(ocount)
    print(zero[num], end=" ")
    print(one[num])
    
t = int(input())
zero = [1,0,1]
one = [0,1,1]

for i in range(t) :
    num = int(input())
    getZeroOne(num)
