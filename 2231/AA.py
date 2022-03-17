from dis import dis
import sys
sys.stdin=open("2231/input.txt","r")
import math 

N = int(input())
n=map(int,str(N))

min = N - 9*len(str(N))
if min<1:
    min=1

for i in range(min, N+1): # 189~216
    check = i + sum(map(int, str(i)))

    if N == check:
        print(i)
        break

    if i == N:
        print('0')
                
                