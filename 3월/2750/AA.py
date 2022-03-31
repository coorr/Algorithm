from dis import dis
import sys
sys.stdin=open("2750/input.txt","r")
import math 


n = int(input())
List=[]
for i in range(n):
    List.append(int(input()))
List.sort()
for x in List:
    print(x)
  
                