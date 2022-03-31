
from os import sep
import sys
sys.stdin=open("9093 단어뒤집기/input.txt","r")


n=int(sys.stdin.readline())
stack=[]

for i in range(n):
    List=sys.stdin.readline().split()
    for j in List:
        print(j[::-1], end=' ')
    print()