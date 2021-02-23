import sys

sys.stdin=open("input.txt", "r")

def reverse(x):
    return int(str(x)[::-1])
        

def isPrime(x):
    if x==1:
        return False
    for i in range(2, n+1):
        if x%i ==0:

            return False
    return True
n=int(input())
a=list(map(int, input().split()))

for x in a:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end =' ')








    
    


