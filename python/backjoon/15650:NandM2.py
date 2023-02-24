#N과 M(2)
from itertools import combinations

N, M = map(int, input().split(' '))

for p in combinations(range(1,N+1), M):
    print(' '.join(map(str, p)))