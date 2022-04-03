
import sys
sys.stdin=open("4월/9095 1,2,3더하기/input.txt","r")

def solution(value):
    moneys=[10000,5000,1000,500,100,50,10]
    won = (value / 10) * 10
    i = 0
    counts=[0]
    
    while True:
        if won >= moneys[i]:
            count=(won/moneys[i])
            won = won - moneys[i] * count
            counts.insert(i,count)
        else:
            counts[i] =0
        i+=1
        
        if won == 0:
            for j in range(len(moneys)):
                counts.append(0)
            break
        
    print(moneys, counts)


n=int(input())
print(solution(n))

    
        



    
    
    
    


