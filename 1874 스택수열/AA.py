
from os import sep
import sys
sys.stdin=open("1874 스택수열/input.txt","r")


n=int(sys.stdin.readline())
stack=[]
array=[]
result=['+']
lt=0
rt=0
for i in range(1,n+1):
    stack.append(int(sys.stdin.readline().strip()))
    array.append(i)
stack.append('end')
array.append('end')

while(True):
    if stack[lt] == array[rt]:
        array.pop(rt)
        lt+=1
        rt-=1
        result.append('-')
        if stack[lt] == 'end':
            break
    else:
        rt+=1
        result.append('+')
        if array[rt] == 'end':
            array.pop(rt)
            break
if len(array) != 1:
    print("NO")
else:
    for x in result:
        print(x)
    