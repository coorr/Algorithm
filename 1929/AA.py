from collections import deque
from glob import glob
from msvcrt import kbhit
from os import remove
from re import A, I
import sys
import heapq as hq
import itertools as it
import math 
sys.stdin=open("1929/input.txt","r")

n,m=map(int,input().split())

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            print(i, num, num**0.5)
            if num%i==0:
                return False
        return True
    
for i in range(n, m+1):
    if isPrime(i):
        print("2222",i)
        
                    


    
    
    
                
                