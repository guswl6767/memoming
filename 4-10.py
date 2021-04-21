import sys
sys.stdin=open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))#역수열
a = a[::-1]
ans=[]
for x in a:
    print(x)
    ans.insert(x,n)
    n-=1
    print(ans)


