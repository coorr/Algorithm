
import sys
sys.stdin=open("4월/10809 알파벳찾기/input.txt","r")



arr=list(sys.stdin.readline().strip())
tmp=[-1] * 26

for i in range(len(arr)):
    if tmp[ord(arr[i])-97] == -1:
        tmp[ord(arr[i])-97] = i
print(*tmp)



        



    
    
    
    


