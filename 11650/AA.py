from dis import dis
import sys
sys.stdin=open("11650/input.txt","r")
import math 



n = int(sys.stdin.readline())
array=[]
for i in range(n):
    a,b=map(int,input().split())
    array.append([a,b])
s_array=sorted(array)   
for i in range(n):
    print(s_array[i][0],s_array[i][1])