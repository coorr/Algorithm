import sys
sys.stdin=open("zz/input.txt","r")

a=int(input())
b=int(input())
tmp=[]
cnt=0
for i in range(a,b+1):
    for j in range(1,i+1):
        if i%j==0:
           cnt+=1
    else:
        if cnt==2:
            tmp.append(i)
            cnt=0
        else:
            cnt=0
# print(tmp)
if len(tmp) == 0:
    print(-1)
else:
    print(sum(tmp))
    Min=tmp[0]
    for x in tmp:
        if Min>=x:
            tmp=Min
    print(Min)                   


    
    
    
                
                