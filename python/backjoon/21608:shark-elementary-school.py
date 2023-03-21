# 상어 초등학교
#
# NxN 격자. 학생 N^2 1~N^2 (r,c) r행 c열
# 1ㅡ1 -> N N
# 인접 = 십자
#
# 1. 좋아하는 학생이 가장 많이 인접한 칸으로 정함
# 2. 1이 여러개이면 인접한 칸 중에서 비어있는 칸이 젤 많은 곳으로
# 3. 2가 여러개이면 행이 가작 작은칸, 열이 제일 작은
#
# N은 20 이하
# 20 * 20 * 20
#
# 만족도 -> 순회 0 0, 1, 1 2 10, 3 100, 4 1000

# 1. 그냥 전체 순회를 돌면서 해당 셀을 평가하는 방법
# 2. 나의 favorite 들을 통해 cell을 방문하고 평가하는 방법 - 쉽게 1번으로


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N = int(input())
field = [[0]*N for _ in range(N)]
favorite = dict()
#
#
for i in range(N**2):
    fav_ary = list(map(int, input().split(' ')))
    favorite[fav_ary[0]] = fav_ary[1:5]

max_fav_cnt = 0
# best = [[x, y, 주변에 비어있는 칸 개수]]
best = []
for cur_student, cur_friends in favorite.items():
    max_fav_cnt = 0
    best = []
    for cur_y in range(N):
        for cur_x in range(N):
            if field[cur_y][cur_x] != 0: continue
            # target의 상하좌우 비교하여 best에 꽂기
            cur_fav_cnt = 0
            cur_empty_cnt = 0
            for i in range(4):
                near_x, near_y = cur_x + dx[i], cur_y + dy[i]
                if not (0 <= near_x < N and 0 <= near_y < N): continue
                if field[near_y][near_x] in cur_friends:
                    cur_fav_cnt += 1
                elif field[near_y][near_x] == 0:
                    cur_empty_cnt += 1
            # 작으면 노의미
            if cur_fav_cnt < max_fav_cnt: continue
            # 현재 선호도가 더 높으면 best 배열 초기화
            if cur_fav_cnt > max_fav_cnt:
                max_fav_cnt = cur_fav_cnt
                best = []
            best.append([cur_x, cur_y, cur_empty_cnt])
    # best 안에 후보들을 조건대로 소팅
    # 2. 1이 여러개이면 인접한 칸 중에서 비어있는 칸이 젤 많은 곳으로
    # 3. 2가 여러개이면 행이 가작 작은칸, 열이 제일 작은
    best.sort(key=lambda ary: (-ary[2], ary[1], ary[0]))
    best_cell = best[0]
    field[best_cell[1]][best_cell[0]] = cur_student

res = 0
for cur_y in range(N):
    for cur_x in range(N):
        cur_student = field[cur_y][cur_x]
        cur_friends = favorite[cur_student]
        friends_cnt = 0
        for i in range(4):
            near_x, near_y = cur_x + dx[i], cur_y + dy[i]
            if not (0 <= near_x < N and 0 <= near_y < N): continue
            # 옆에 친구가 있으면 카운팅
            if field[near_y][near_x] in cur_friends:
                friends_cnt += 1
        if friends_cnt >= 1:
            res += 10 ** (friends_cnt-1)
print(res)
