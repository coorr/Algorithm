
import sys
sys.stdin=open("4월/9095 1,2,3더하기/input.txt","r")



n=int(input())  
arr=list(sys.stdin.readline().split())
arr.insert(0,0)
dy=[0] * (n + 1)
dy[1]=1
print(arr)
print(dy)
res=0 
for i in range(2,n+1):
    Max=0
    for j in range(i-1,0,-1):
        if arr[i] > arr[j] and dy[j]>Max:
            Max=dy[j]
    dy[i]=Max+1
    
    if dy[i]>res:
        res=dy[i]
print(res)

              



    
    
    
    


