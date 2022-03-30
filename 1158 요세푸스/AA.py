
import sys
sys.stdin=open("1158 요세푸스/input.txt","r")



a,b=map(int,input().split())
que=list(range(1, a+1))
tmp=[]
idx=b - 1
while que:
    if idx >= len(que):
        idx %= len(que)
    else:
        tmp.append(que.pop(idx))
        idx += b - 1
        
# result = f'<{", ".join(tmp)}>'
# print(result)
print("<", ', '.join(str(i) for i in tmp), ">",sep='')
    
     
        
    




        

            

        
