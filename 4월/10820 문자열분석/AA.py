
import sys
sys.stdin=open("4월/10820 문자열분석/input.txt","r")



while True:
    arr=list(sys.stdin.readline().rstrip('\n'))
    a,b,c,d=0,0,0,0
    if not arr:
        break
    else:
        for i in arr:
            if i.isupper():
                b+=1
            elif i.islower():
                a+=1
            elif i.isdigit():
                c+=1
            elif i.isspace():
                d+=1
    print(a,b,c,d, end='\n')



        



    
    
    
    


