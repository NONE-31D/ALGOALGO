m, n = map(int, input().split())

gcd = 0
lcm = 0

a = m
b = n
if a < b:
    (a, b) = (b, a)
while b != 0:
    (a, b) = (b, a % b)
gcd = a
lcm = int(m*n/gcd)

print(gcd)
print(lcm)
