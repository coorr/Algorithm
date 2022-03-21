from dis import dis
import sys
sys.stdin=open("2751/input.txt","r")
import math 


n = int(input())
List=[]
for i in range(n):
    List.append(int(sys.stdin.readline()))
List.sort()
for i in List:
    print(i)
  
                