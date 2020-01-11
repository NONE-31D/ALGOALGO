a,b,c = map(int, input().split())

if b>=c :
    print(-1)
else :
    print(a//(c-b)+1) // 손익분기점 = (고정비용/노트북 한대 당 순이익) + 1
