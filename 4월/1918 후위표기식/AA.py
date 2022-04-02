
import sys
sys.stdin=open("4월/1918 후위표기식/input.txt","r")



arr=list(sys.stdin.readline())
stack=[]
res=''
for x in arr:
    if 'A' <= x <= 'Z':
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1] != '(':
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1] != '(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)
        



    
    
    
    


