import sys

def solution(lt, rt):
    if lt<rt:
        for i in range(lt,rt):
            for j in range(i, 0 ,-1):
                if arr[j-1] > arr[j]:
                    arr[j-1] , arr[j] = arr[j], arr[j-1]
        

if __name__=="__main__":
    arr=[23,11,45,36,15,67,33,21,19]
    solution(1, len(arr))
    print(arr)
    

        



    
    
    
    


