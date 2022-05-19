import sys

def solution(rt):
    for i in range(rt):
        for j in range(rt-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__=="__main__":
    arr=[23,11,45,36,15,67,33,21]
    solution(len(arr))
    print(arr)
    

        



    
    
    
    


