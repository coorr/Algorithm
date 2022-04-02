
import sys
sys.stdin=open("4월/10808 알파벳 개수/input.txt","r")



arr=list(sys.stdin.readline().strip())
tmp=[0] * 26

for i in range(len(arr)):
    tmp[ord(arr[i])-97] += 1
print(*tmp)



        



    
    
    
    


