
import sys
sys.stdin=open("4월/17299 오등큰수/input.txt","r")


n=int(input())
arr=list(map(int,sys.stdin.readline().split()))
tmp=[0]
answer= [-1] * n
List={}

cnt={}
for i in arr:
    try: cnt[i]+=1
    except: cnt[i]=1
arr_cnt=[0] * n

for i in range(n):
    arr_cnt[i]=cnt[arr[i]]

for i in range(1,n):
    while tmp and arr_cnt[tmp[-1]] < arr_cnt[i]:
        answer[tmp.pop()] = arr[i]
    tmp.append(i)
print(*answer)

        



    
    
    
    


