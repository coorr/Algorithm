import sys
sys.stdin=open("3월/1929/input.txt","r")

n,m=map(int,input().split())

def isPrime(num):
    print(num)
    if num==1:
        return False
    else:
        print(int(num**0.5)+1)
        for i in range(2, int(num**0.5)+1):
            print(i, num, num**0.5)
            if num%i==0:
                return False
        return True
    
for i in range(n, m+1):
    if isPrime(i):
        print("2222",i)
        
                    


    
    
    
                
                