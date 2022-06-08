def solution(s):
    answer = ''
    List = list(map(str, s.split(' ')))
    result =[]
    for x in List:
        if x[:1].isalpha():
            print(x[:1])
            x = x.capitalize()
            print(x)
            result.append(x)
        else:
            x = x.lower()
            result.append(x)
    answer = ' '.join(result)
    return answer

print(solution("3people unFollowed me"))