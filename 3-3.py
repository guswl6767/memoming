import sys
sys.stdin=open("input.txt", "r")
a=list(range(21))#0부터 20까지 자동으로 list
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i]= a[e-i], a[s+i]#swap
a.pop(0)#맨앞자리 0 없애기 빈칸으로 냅두면 뒤에가 없어짐
for x in a:
    print(x, end=' ')

   

    

    


