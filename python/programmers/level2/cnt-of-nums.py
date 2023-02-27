# 연속 부분 수열 합의 개수

def solution(elements):
    answer = set()
    N = len(elements)

    for i in range(N):
        sums = 0
        for cnt in range(0, N):
            sums += elements[(i + cnt) % N]
            answer.add(sums)

    answer.add(sum(elements))
    return len(answer)