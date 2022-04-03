
import sys
sys.stdin=open("4월/11726 2xn타일링/input.txt","r")



n=int(input())
dy=[0] * (n+2)
dy[1]=1
dy[2]=2
res=0
for i in range(2,n+2):
    dy[i]=2*dy[i-2]+dy[i-1]
    if dy[i]>res:
        res=dy[i]
print(res%10007)

    
        



    
    
    
    


