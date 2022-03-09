from collections import deque
from glob import glob
from msvcrt import kbhit
from os import remove
from re import A, I
import sys
import heapq as hq
import itertools as it
import math 
sys.stdin=open("11653/input.txt","r")

n=int(input())
if n == 1:
    print('')
    
for i in range(2,n+1):
    if n%i==0:
        while n%i==0:
            print(i)
            n = n // i
    
                    


    
    
    
                
                