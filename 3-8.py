import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a= [list(map(int,input().split()))for _ in range(n)]
m=int(input())

for i in range(m):
    e,r,t = map(int,input().split())
    if r==0:
        for _ in range(t):

            a[e-1].append(a[e-1].pop(0))#pop(0)은 0번째 인덱스 값을 가져오고 비어있는 0번쨰 인덱스에는 뒤에 숫자들이 한칸씩 땡겨서 들어와짐
    else:
        for _ in range(t):
            a[e-1].insert(0,a[e-1].pop())

res=0
s=0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
        
print(res)
