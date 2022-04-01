

import sys
sys.stdin=open("4월/17298 오큰수/input.txt","r")


n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
stack=[]
stack.append(0)
answer= [-1] * n

for i in range(1,n):
    while stack and arr[i] > arr[stack[-1]]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
    
print(*answer)



    
    
    
    


