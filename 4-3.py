import sys
sys.stdin=open("input.txt", "r")

def Count(mid):
    cnt=1#dvd한장이 필요하다
    sum=0
    for x in a:
        if sum+x>mid:#sum 누적시간 
            cnt+=1 #새로운 dvd필요
            sum=x#sum초기화
        else:
            sum+=x

    return cnt
n, m = map(int, input().split())
a = list(map(int,input().split()))
maxx=max(a)

lt=1
rt=sum(a)
res=0


while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:#dvd용량이 9보다는 크거나 같아야 노래가 들어감
        res=mid
        rt=mid-1
    else:
        lt=mid+1#용량이 너무 작아서 큰쪽이 필요함 그래서 lt+1
print(res)

