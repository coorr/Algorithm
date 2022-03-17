from dis import dis
import sys
sys.stdin=open("7568/input.txt","r")
import math 

n = int(input())
List=[]
cnt=0
for _ in range(n):
    a,b=map(int,input().split())
    List.append((a,b))
for c in List:
    rank=1
    
    for x in List:
        if c[0] != x[0] and c[1] != x[1]:
            if c[0] < x[0] and c[1] < x[1]:
                # print(c[0], x[0])
                rank +=1
        
    print(rank)

                