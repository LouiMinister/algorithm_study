# [카카오 인턴] 경주로 건설
import heapq

MAX_V = 999999999999999


def solution(board):
    N = len(board)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    costs = [[[MAX_V, MAX_V, MAX_V, MAX_V] for _ in range(N)] for _ in range(N)]

    queue = []
    heapq.heappush(queue, (0, 0, 0, 0))  # x, y, cost, 방향배열 (x+1: 0 y+1: 1 x-1: 2 y-1: 3)
    heapq.heappush(queue, (0, 0, 0, 1))

    while queue:
        # print(queue)
        cur_x, cur_y, cur_cost, cur_direction = heapq.heappop(queue)
        # print(costs[cur_y][cur_x][cur_direction], cur_cost)
        if costs[cur_y][cur_x][cur_direction] <= cur_cost: continue
        costs[cur_y][cur_x][cur_direction] = cur_cost
        # costs 에 반영

        # cur_x, cur_y 기준으로 순회
        for i in range(4):

            next_x, next_y, next_direction = cur_x + dx[i], cur_y + dy[i], i
            # 상한 하한에 닿으면 탈출
            if not (0 <= next_x < N and 0 <= next_y < N): continue
            # 벽에 닿으면 탈출
            if board[next_y][next_x] == 1: continue
            # print(next_x, next_y, next_direction)

            next_cost = None

            if next_direction == cur_direction:
                next_cost = cur_cost + 100
            # 꺾였을 경우
            elif (next_direction + 1) % 4 == cur_direction or (next_direction + 3) % 4 == cur_direction:
                next_cost = cur_cost + 600
            # costs랑 비교했을 때 작으면 queue에 푸시 ?
            if next_cost != None:
                if costs[next_y][next_x][next_direction] > next_cost:
                    heapq.heappush(queue, (next_x, next_y, next_cost, next_direction))

    # print(costs)
    return min(costs[N - 1][N - 1])


