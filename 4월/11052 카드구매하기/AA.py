
import sys
sys.stdin=open("4월/11052 카드구매하기/input.txt","r")

N = int(input())
p = [0] + list(map(int,input().split()))
dp = [999999999 for i in range(1001)]
dp[0] = 0


for i in range(N+1):
    for k in range(i+1):
        dp[i] = min(dp[i], dp[i-k] + p[k])
print(dp[N])

    
        



    
    
    
    


