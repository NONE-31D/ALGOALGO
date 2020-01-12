def gcd(a, b):
    if b<=0 :
        return a
    
    tmp=a%b #나머지
    return gcd(b,tmp)

def lcm(a, b):
    return (a*b)/gcd(a, b)

a, b = input().split()
a = int(a)
b = int(b)
#a = int(input())
#b = int(input())


if a>b:
    print("%d\n%d" % (gcd(a,b), lcm(a,b)))
else:
    print("%d\n%d" % (gcd(b,a), lcm(b,a)))
