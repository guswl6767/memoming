import sys
sys.stdin=open("input.txt", "r")

def Count(mid):
    cnt=1
    hs=horse[0]
    for i in range(n):
        if horse[i]-hs>=mid:
            cnt+=1
            hs=horse[i]
    return cnt

n,c = map(int, input().split())

horse=[]
for x in range(n):
    tmp=int(input())
    horse.append(tmp)
horse.sort()

lt=1
rt=horse[n-1]
res=0
while lt<=rt:
    mid=(lt+rt)//2#mid가 가장가까운 두 말의 거리
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)
