# 무지의 먹방 라이브

import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    pq = []
    for i in range(len(food_times)):
        heapq.heappush(pq, (food_times[i], i+1))

    prev_dec_sum = 0
    while True:
        smallest_time = pq[0][0] - prev_dec_sum
        decrease = len(pq) * smallest_time
        if k >= decrease:
            k -= decrease
            prev_dec_sum += smallest_time
            heapq.heappop(pq)
        else:
            break
    pq.sort(key=lambda v: v[1])
    return pq[k % len(pq)][1]

print(solution([1, 2, 3], 5))