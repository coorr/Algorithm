

import sys
sys.stdin=open("4월/10799 쇠막대기/input.txt","r")



arr=list(sys.stdin.readline().strip())
tmp=[]
sum=0
for i in range(len(arr)):
    if arr[i] == '(':
        tmp.append(arr[i])
    elif arr[i-1] != arr[i]  :
        tmp.pop()
        sum+=len(tmp)
    elif arr[i-1] == arr[i]:
        tmp.pop()
        sum+=1
print(sum)


    
    
    
    


