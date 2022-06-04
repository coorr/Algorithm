def solution(phone_number):
    answer = ''
    result = phone_number[:-1]
    print(result)
    answer = "*" * (len(phone_number) - 4)
    print(answer)
    answer += phone_number[-4:]
    print(answer)
    return answer

print(solution("01033334444"))