import sys
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
people = list(map(int, input().split()))
people.sort()

cnt=0
while people:
    if len(people)==1:
        cnt+=1
        break
    if people[0]+people[-1]>m:
        people.pop()
        cnt+=1
    else:
        people.pop(0)
        people.pop()
        cnt+=1

print(cnt)




