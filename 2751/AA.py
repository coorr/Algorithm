from dis import dis
import sys
sys.stdin=open("2751/input.txt","r")
import math 


# n = int(input())
# List=[]
# for i in range(n):
#     List.append(int(sys.stdin.readline()))
# List.sort()
# for i in List:
#     print(i)



def Dsort(lt,rt):
    if lt<rt:
        mid=(lt+rt)//2
        Dsort(lt,mid)
        Dsort(mid+1,rt)
    
        p1=lt
        p2=mid+1
        tmp=[]
        while p1<=mid and p2<=rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1
        if p1<=mid: tmp=tmp+arr[p1:mid+1]
        if p2<=rt: tmp=tmp+arr[p2:rt+1]
        for i in range(len(tmp)):
            arr[lt+i]=tmp[i]
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
Dsort(0,n-1)
for x in arr:
    print(x)       
  
# if __name__=="__main__":
#     n=int(input())
#     arr=[]
#     for i in range(n):
#         arr.append(int(input()))
#     Dsort(0,4)
#     for x in arr:
#         print(x)  