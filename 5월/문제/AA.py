from ast import Return
import sys
sys.stdin=open("5월/문제/input.txt","r")

stack=list(sys.stdin.readline().strip())
second=[]
n=int(sys.stdin.readline())

for _ in range(n):
    command=list(sys.stdin.readline().split())
    
    if command[0] == 'L':
        if stack:
            second.append(stack.pop())
    elif command[0] == 'D':
        if second:
            stack.append(second.pop())
    elif command[0] == 'B':
        if stack:
            stack.pop()
    else:
        stack.append(command[1])
stack.extend(reversed(second))
for x in stack:
    print(x, end='')