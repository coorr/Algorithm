
from os import sep
import sys
sys.stdin=open("18870/input.txt","r")


n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
arr2=[]

arr2=list(sorted(set(arr)))

dic={arr2[i]:i for i in range(len(arr2))}

for x in arr:
    print(dic[x], end=' ')   