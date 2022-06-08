def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        List = list(skill)
        for s in skills:
            if s in skill:
                if s != List.pop(0):
                    break
        else: 
            answer +=1
            
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))