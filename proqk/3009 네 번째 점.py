x=[]
y=[]

for i in range(3):
    xx,yy = input().split()
    x.append(xx)
    y.append(yy)

for i in range(3):
    if x.count(x[i])==1:
        x_=x[i]
    if y.count(y[i])==1:
        y_=y[i]
print(x_,y_)
