from dis import dis
import sys
sys.stdin=open("10870/input.txt","r")
import math 

def solution(n):
    if n<=1:
        return n
    
    return solution(n-1) + solution(n-2)

if __name__=="__main__":
    n=int(input())
    
    
    print(solution(n))


                
                