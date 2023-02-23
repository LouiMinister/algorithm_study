#1, 2, 3 더하기
tcc = int(input())
tc = []
for _ in range(tcc):
    tc.append(int(input()))

memo = [0, 1, 2, 4] + ([0] * max(tc))
for i in range(4, max(tc) + 1):
    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

for t in tc:
    print(memo[t])
