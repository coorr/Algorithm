from dis import dis
import sys
sys.stdin=open("11729/input.txt","r")
import math 

def solution(n, start,end):
    if n==1:
        print(start,end)
        return
    solution(n-1, start, 6-start-end)
    print(start,end)
    solution(n-1, 6-start-end, end)

n=int(input())
print((2**n)-1)
solution(n, 1, 3)

                
                