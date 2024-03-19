
# 최대 시간.
# 255명이 255칸 dfs - 255시간동안 <= 1억

# 입력
n, m = map(int, input().split(' ')) # 격자의 크기 2~15, 사람의 수 1~225
grid = [list(map(int, input().split())) for _ in range(n)]
conv = [] # 겹치지 않음. 편의점 위치와 베이스 캠프도 겹치지 않음
for _ in range(m):
    tmp = list(map(int, input().split()))
    conv.append((tmp[1], tmp[0]))

player = [] # 사람 위치 (x,y)



# n번 사람은 n분에 출발함
# 이동
    # 1 최단거리로 1칸 움직임. 위 좌 우 하
    # 2 편의점에 도착하면 멈춤. 이제 이 편의점 칸을 지나갈 수 없음
    # 3 if 현재 시간 t <= 사람의 수
        # t번 사람 - 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프 들어감(같다면 y가 작은 같다면 x가 작은)
        # 이동 시간 소요 X
        # 그 이후로 베이스캠프 칸 지나갈 수 없음.  나오더라도 불가능

# 출력
    #모든 사람이 도착하는 시간