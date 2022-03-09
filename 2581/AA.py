from collections import deque
from glob import glob
from msvcrt import kbhit
from os import remove
from re import A, I
import sys
import heapq as hq
import itertools as it
import math 
sys.stdin=open("zz/input.txt","r")

a=int(input())
b=int(input())
tmp=[]
cnt=0
for i in range(a,b+1):
    for j in range(1,i+1):
        if i%j==0:
           cnt+=1
    else:
        if cnt==2:
            tmp.append(i)
            cnt=0
        else:
            cnt=0
# print(tmp)
if len(tmp) == 0:
    print(-1)
else:
    print(sum(tmp))
    Min=tmp[0]
    for x in tmp:
        if Min>=x:
            tmp=Min
    print(Min)                   


    
    
    
                
                