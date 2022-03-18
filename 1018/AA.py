from dis import dis
import sys
sys.stdin=open("1018/input.txt","r")
import math 

N, M = map(int, input().split())
board=list()
for p in range(N):
    board.append(input())
tmp=list()
for k in range(N-7):
    for l in range(M-7):
        first_W=0
        first_B=0
        for i in range(k,k+8):
            for j in range(l,l+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        first_W = first_W+1
                    if board[i][j] != 'B':
                        first_B = first_B + 1
                else:
                    if board[i][j] != 'B':
                        first_W = first_W+1
                    if board[i][j] != 'W':
                        first_B = first_B + 1
        tmp.append(first_W)
        tmp.append(first_B)
print(min(tmp))
                 
                