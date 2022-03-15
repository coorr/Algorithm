from dis import dis
import sys
sys.stdin=open("10872/input.txt","r")
import math 

n=int(input())

Sum= 1
for i in range(n):
    if n==0:
        print(1)
    else:
        Sum += Sum *i
print(Sum)


                
                