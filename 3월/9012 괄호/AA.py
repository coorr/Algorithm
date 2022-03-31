
from os import sep
import sys
sys.stdin=open("9012 괄호/input.txt","r")


n=int(sys.stdin.readline())
stack=[]
for i in range(n):
    List=list(sys.stdin.readline().strip())
    cnt=0
    for j in List:
        if j == '(':
            cnt+=1
        elif j == ')' and cnt > 0:
            cnt-=1
        elif j == ')':
            print("NO")
            break
            
    else:
        if cnt == 0:
            print("YES")
        else:
            print("NO")
