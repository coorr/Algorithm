import sys
sys.stdin=open("5월/병합정렬/input.txt","r")

def solution(lt, rt):
    if lt<rt:
        mid=(lt + rt ) // 2
        
        solution(lt, mid)
        solution(mid+1, rt)
        tmp=[]
        p1=lt
        p2=mid+1
        while p1<=mid and p2 <=rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1
        if p1<=mid: tmp=tmp+arr[p1:mid+1]
        if p2<=rt: tmp=tmp+arr[p2: rt+1]
        
        for i in range(len(tmp)):
            arr[lt+i] = tmp[i]

if __name__=="__main__":
    arr=[23,11,45,36,15,67,33,21]
    solution(0, len(arr)-1)
    print(arr)
    

        



    
    
    
    


