import sys
#sys.stdin=open("input.txt", "r")
n = int(input())
for i in range(n):
    str= input()
    str = str.lower()
    if str == str[::-1]:
        print("YES")
    else:
        print("NO")


     

