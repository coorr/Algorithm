import sys

def solution(record):
    answer = []
    uid = []
    uidMap = {}
    for x in record:
        a= x.split()
        if a[0] == "Enter":
            uidMap[a[1]] = a[2]
            uid.append(a[1])
            answer.append( a[2]+"님이 들어왔습니다.")
        if a[0] == "Leave":
            uid.append(a[1])
            answer.append( uidMap[a[1]]+"님이 나갔습니다.")
        if a[0] == "Change":
            uidMap[a[1]] = a[2]

    for i in range(len(uid)):
        username = uidMap[uid[i]]
        if answer[i][len(answer[i]) - 7:] == "들어왔습니다.":
            answer[i] = username+"님이 들어왔습니다."
        else:
            answer[i] = username+"님이 나갔습니다."
            
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
    

        



    
    
    
    


