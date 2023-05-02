class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        while True:
            if n in memo: return False
            else: memo.add(n)
            nxt_n = 0
            for v in map(int, str(n)):
                nxt_n += v**2
            n = nxt_n
            if n == 1:
                return True
        return False


# happy number
# 양수 -> 각 자릿수의 제곱의 합
# 1이 될 때 까지 반복
# 1로 끝나면 happy number

# 2 4 16 37 63 45 41 
