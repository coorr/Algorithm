
import sys
from collections import deque
sys.stdin=open("10866 덱/input.txt","r")



n=int(sys.stdin.readline())
array=deque([])

for _ in range(n):
    command=sys.stdin.readline().split()
    
    if command[0] == 'push_back':
        array.append(command[1])
    elif command[0] == 'push_front':
        array.appendleft(command[1])
    elif command[0] == 'pop_front':
        if array: 
            print(array.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if array:
            print(array.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(array))
    elif command[0] == 'empty':
        if array:
            print(0)
        else:
            print(1)
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
    




        

            

        
