import sys
sys.stdin=open("input.txt", "r")
n = (input())
cnt=0
for x in n:
  
    if x.isdigit():
        cnt = cnt*10+int(x)
print(cnt)
res=0
for i in range(1, cnt+1):
    if cnt%i==0:
        res +=1
print(res)

    

    


