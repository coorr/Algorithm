
import sys
sys.stdin=open("4월/1935 후위표기식2/input.txt","r")

n=int(sys.stdin.readline())
arr=list(sys.stdin.readline().strip())
num_lst = [0]*n				
for i in range(n):
    num_lst[i] = int(input())
stack=[]
for x in arr:
    if 'A' <= x <= 'Z':
        stack.append(num_lst[ord(x)-ord('A')])
    else:
        if x=='+':
            num = stack[-2] + stack[-1]
            stack.pop()
            stack.pop()
            stack.append(num)
        elif x=='-':
            num = stack[-2] - stack[-1]
            stack.pop()
            stack.pop()
            stack.append(num)
        elif x=='*':
            num = stack[-2] * stack[-1]
            stack.pop()
            stack.pop()
            stack.append(num)
        else:
            num = stack[-2] / stack[-1]
            stack.pop()
            stack.pop()
            stack.append(num)
    
print('%.2f' %stack[0])
        
    
                         


        



    
    
    
    


