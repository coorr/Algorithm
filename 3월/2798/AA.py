from dis import dis
import sys
sys.stdin=open("2798/input.txt","r")
import math 

n,k=map(int,input().split())
List=list(map(int,input().split()))
cnt=0
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            if cnt < List[i]+List[j]+List[m] <= k:
                cnt=List[i]+List[j]+List[m]
print(cnt)

                
                