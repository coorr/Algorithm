from ast import Return
import sys
sys.stdin=open("5월/에디터/input.txt","r")

n=int(input())

stack=[]
array=[]
result=["+"]
lt=0
rt=0
for i in range(1,n+1):
    stack.append(int(input()))
    array.append(i)

stack.append('end')
array.append('end')

while(True):
    if stack[lt] == array[rt]:
        array.pop(rt)
        lt+=1
        rt-=1
        
        result.append("-")  
        if stack[lt] == 'end':
            break      
    else:
        rt+=1
        result.append("+")
        if array[rt] == 'end':
            break
        
if len(array) != 1:
    print("NO")
else:
    for x in result:
        print(x)
