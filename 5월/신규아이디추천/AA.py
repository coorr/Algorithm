import re 

def solution(user_id):
    user_id = remove_unique(user_id)
    if len(user_id) == 0:
        user_id = "a"
    if len(user_id) >= 16:
        user_id= user_id[:15]
        if user_id[-1] == ".":
            user_id= user_id[:14]
            
    if len(user_id) <= 2:
        for _ in range(3-len(user_id)):
            user_id += user_id[-1]
            
    
    return user_id

def remove_unique(user_id):
    user_id = user_id.lower()
    user_id = re.sub(r"[^a-zA-Z0-9_\.-]",'',user_id)
    user_id = re.sub(r"\.+",".",user_id)
    user_id = re.sub(r"^[.]|[.]$",'',user_id)
    if user_id[-1] == ".":
        user_id = user_id.replace(user_id[-1],"")

    return user_id

print(solution("...!@BaT#*..y.abcdefghijklm"))

        



    
    
    
    


