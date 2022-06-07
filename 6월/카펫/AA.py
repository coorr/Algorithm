def solution(brown, yellow):
    answer = []
    for i in range(brown+yellow):
        for j in range(i+1):
            if 2 *i + 2 * j  - 4 == brown:
                if i * j - brown == yellow:
                    answer.append(i)
                    answer.append(j)
                    return answer
    return answer

print(solution(10,2))