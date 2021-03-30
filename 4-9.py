import sys
sys.stdin=open("input.txt", "r")

n = int(input())
a = list(map(int,input().split()))

lt=0
rt=n-1
cp=0
tmp=[]
res=""#문자열 누적

while lt<=rt:
    if a[lt]>cp:
        tmp.append((a[lt],'L'))
    if a[rt]>cp:
        tmp.append((a[rt],'R'))
    tmp.sort()
    if len(tmp)==0:
        break;

    else:
        res=res+tmp[0][1]
        cp=tmp[0][0]
        if tmp[0][1]=='L':
            lt=lt+1
        else:
            rt=rt-1
    tmp.clear()
print(len(res))
print(res)





