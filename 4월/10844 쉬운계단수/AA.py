

import sys
sys.stdin=open("4월/10844 쉬운계단수/input.txt","r")

n = int(input())
List=[list(map(int,input().split())) for _ in range(n)]
dy=[[0] * n for _ in range(n    )]
dy[0][0]=List[0][0]


for i in range(1,n):
    dy[0][i] = dy[0][i-1] + List[0][i]
    dy[i][0] = dy[i-1][0] + List[i][0]
for i in range(1,n):
    for j in range(1,n):
        dy[i][j] = max(dy[i-1][j], dy[i][j-1])+List[i][j]

for x in dy:
    print(x)
print(dy[n-1][n-1])

    
    
    
    


