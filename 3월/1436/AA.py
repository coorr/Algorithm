from dis import dis
import sys
sys.stdin=open("1436/input.txt","r")
import math 


n = int(input())
nth=666
cnt=0

while True:
    if '666' in str(nth): # 666 1666 2666 3666 4666
        cnt+=1
    if cnt==n:
        print(nth)  
        break
    nth+=1
  
                