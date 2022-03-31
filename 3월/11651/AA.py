
import sys
sys.stdin=open("11651/input.txt","r")

n = int(sys.stdin.readline())
array=[]
for i in range(n):
    a,b=map(int,input().split())
    array.append([a,b])
array.sort(key=lambda x: (x[1],x[0]))
for i in range(n):
    print(array[i][0],array[i][1])