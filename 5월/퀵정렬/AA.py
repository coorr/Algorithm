import sys

def solution(lt, rt):
    if lt<rt:
        pivot = arr[rt]
        pos = lt
        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos] , arr[i]
                pos+=1

        arr[pos], arr[rt] = arr[rt] , arr[pos]
        solution(lt, pos - 1)
        solution(pos + 1 , rt)
        

if __name__=="__main__":
    arr=[23,11,45,36,15,67,33,21,19]
    solution(0, len(arr)-1)
    print(arr)
    

        



    
    
    
    


