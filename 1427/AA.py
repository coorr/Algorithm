from dis import dis
import sys
sys.stdin=open("1427/input.txt","r")
import math 



n = map(int,input())
List=[]


for i in n:
    List.append(i)
for x in range(len(List)):
    print(max(List), end='')
    List.remove(max(List))                