import sys

answer = 0
def DFS(idx, result, numbers, target):
    global answer
    if idx == len(numbers):
        if result == target:
            answer+=1
        else: return 0
    else:
        DFS(idx+1, result+numbers[idx], numbers, target)
        DFS(idx+1, result-numbers[idx], numbers, target)

def solution(numbers, target):
    global answer
    DFS(0, 0, numbers, target)
    return answer

print(solution([1, 1, 1, 1, 1], 3))

        



    
    
    
    


