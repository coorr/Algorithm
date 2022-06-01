from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * (len(id_list))
    
    Set = defaultdict(set)
    List = defaultdict(int)
    for x in report:
        a, b = x.split()
        Set[a].add(b)
    for x in Set.values():
        for y in x:
            List[y] += 1
    
    for idx, x in enumerate(id_list):
        for y in Set[x]:
            if List[y] >= k:
                answer[idx] +=1
        
        
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))

        



    
    
    
    


