import sys
sys.stdin=open("input.txt", "r")

n = int(input())
man = []

for i in range(n):
    s ,e = map(int, input().split())
    man.append((s,e))
man.sort(reverse=True)
cnt=0
lt=0
rt=0
for s, e in man:
    if s>=lt or e>=rt:
        lt=s 
        rt=e
        cnt+=1

print(cnt)
