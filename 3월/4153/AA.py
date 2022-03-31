import sys
sys.stdin=open("4153/input.txt","r")

while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    if c*c == a*a+b*b or a*a+c*c==b*b or b*b+c*c==a*a:
        print('right')
    else:
        print('wrong')
    
    
                
                