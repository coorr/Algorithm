from ast import Return
import re
import sys
sys.stdin=open("5월/문제/input.txt","r")

def DFS(n):
    if n > 7:
        return 
    else:
        DFS(n * 2)
        DFS(n * 2 + 1)
        

if __name__=="__main__":
    DFS(1)


                