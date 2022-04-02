
import sys
sys.stdin=open("4월/11656 접미사배열/input.txt","r")

arr=list(sys.stdin.readline().strip())
tmp=[]
while True:
    res=''
    for i in range(len(arr)):
        res+=arr[i]
    tmp.append(res)
    arr.pop(0)
    if len(arr) ==0:
        break
tmp.sort()
print(*tmp)





        



    
    
    
    


