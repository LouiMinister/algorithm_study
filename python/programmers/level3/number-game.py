# 숫자 게임
def solution(A, B):
    result = 0
    N = len(A)
    A.sort(reverse=True)
    B.sort(reverse=True)

    A_i, B_i = 0, 0
    while A_i < N:
        if A[A_i] < B[B_i]:
            result += 1
            B_i += 1
        A_i += 1
    return result