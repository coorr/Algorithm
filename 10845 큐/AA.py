
import sys
from collections import deque
sys.stdin=open("10845 큐/input.txt","r")



n=int(sys.stdin.readline())
array=deque([])

for _ in range(n):
    command=sys.stdin.readline().split()
    
    if command[0] == 'push':
        array.append(command[1])
    elif command[0] == 'front':
        if array:
            print(array[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if array:
            print(array[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(array))
    elif command[0] == 'empty':
        if len(array) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'pop':
        if len(array) == 0:
            print(-1)
        else:
            print(array.popleft())
        
# print(array)
        
    




        

            

        
