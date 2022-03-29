
import sys
sys.stdin=open("10814/input.txt","r")


n=int(sys.stdin.readline())
List=[]
for i in range(n):
    a,b=sys.stdin.readline().split()
    a=int(a)
    List.append([a,b,i])
List.sort(key=lambda x: (x[0] , x[2]))
for x in List:
    print(x[0],x[1])
                
                