from collections import defaultdict
def solution(answers):
    one = [1,2,3,4,5]
    two = [2, 1, 2, 3, 2, 4, 2, 5] 
    three  = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    score = [0,0,0] 
    result = []
    
    
    for i in range(len(answers)):
        if one[i%len(one)] == answers[i]:
            score[0]+=1
        if two[i%len(two)] == answers[i]:
            score[1]+=1
        if three[i%len(three)] == answers[i]:
            score[2]+=1
    
    for idx,x in enumerate(score):
        if x == max(score):
            result.append(idx+1)
            
    return result

print(solution([1,2,3,4,5]))