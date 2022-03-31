import sys
sys.stdin=open("4948/input.txt","r")

def sosu(x):
    if x==1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True

all_list = list(range(2, 246912))
memo=[]

for i in all_list:
    if sosu(i):
        memo.append(i)

while True:
    n=int(input())
    num=n*2
    cnt=0
    
    
    if n==0:
        break
    
    for i in memo:
        if n < i <= num:
            cnt+=1
    print(cnt)
            

    
          


        
                    


    
    
    
                
                