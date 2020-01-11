// 최대공약수 (유클리드 호제법 활용)
def gcd(a,b) : 
    if a < b :
        a,b = b,a
    while true :
        mod = a % b
        if mod == 0 :
            return b
        else :
            a,b = b,mod

// 최소공배수
def lcm(a,b) :
    return int((a*b)/gcd(a,b))

a,b = map(int, input().split())
print(gcd(a,b))
print(lcm(a,b))
