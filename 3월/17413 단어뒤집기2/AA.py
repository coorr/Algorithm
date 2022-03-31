

import sys
sys.stdin=open("3월/17413 단어뒤집기2/input.txt","r")



arr=list(sys.stdin.readline().strip())
cnt=0
tmp=[]
test=""
Len = len(arr)

for i in range(Len):
    
    if arr[i] == '<' and len(test) > 0 and cnt ==0:
        print(test[::-1],end='')
        test=""

    if arr[i] == '<':
        cnt+=1
        print(arr[i], end='')
    elif arr[i] == '>':
        cnt-=1
        print(arr[i], end='')
    elif cnt > 0: 
        print(arr[i], end='')
    else:
        if arr[i] == ' ' or i+1 == Len:
            if arr[i] != ' ':
                test=test+arr[i]
                print(test[::-1],end='')
                continue
            print(test[::-1]+arr[i],end='')
            test=""
        else:
            test=test+arr[i]
    
    
    
    


