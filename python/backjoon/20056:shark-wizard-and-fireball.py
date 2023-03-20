# N N 격자에 M개 발사
# i번 파이어볼 위치 - ri, ci, 질량 - mi, 방향 si, 속력 di
# 방향 - 8방향, 행렬 1~N 번호
#
# 1. 이동 - di, si
# 2. 같은칸 파이어볼 모두 합쳐짐.
#     파이어볼은 4개의 파이어볼로 나눠짐
#     질량 = 합쳐진 파이어볼 질량합/5
#     속력 합쳐진 파이어볼 속력합/ 합쳐진 파이어볼 개수
#     합쳐진 파이어볼 방향 모두 홀수 or 짝수 -> 0, 2, 4 ,6 else 1, 3, 5, 7
#     질량이 0인 파이어볼은 소멸
#
# K 번 이동 후 남아있는 파이어볼 질량합 구하기
import math
from functools import reduce

field_size, fireball_cnt, attempts = map(int, input().split(' '))

# cell = {cur: [[m,d,s]], next: [[m,d,s],[m,d,s]]}
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
field = [[{"cur": [], "next": []} for _ in range(field_size+1)] for _ in range(field_size+1)]
for _ in range(fireball_cnt):
    r, c, m, s, d = map(int, input().split(' '))
    field[r][c]['cur'].append([m, s, d])

def print_field():
    global field, field_size
    for f in field:
        print(f)
    print(' ')


# print_field()
for _ in range(attempts):
    # 이동
    for i in range(1, field_size+1):
        for j in range(1, field_size+1):
            for fireball in field[i][j]['cur']:
                cur_m, cur_s, cur_d = fireball
                next_y, next_x = i + dy[cur_d] * cur_s, j + dx[cur_d] * cur_s
                # 범위 체크
                next_y = (next_y - 1 + field_size*1000) % field_size + 1
                next_x = (next_x - 1 + field_size*1000) % field_size + 1
                # if not (1 <= next_y <= field_size and 1 <= next_x <= field_size): continue
                # 이동
                field[next_y][next_x]['next'].append([cur_m, cur_s, cur_d])

    # 2. 같은칸 파이어볼 모두 합쳐짐.
    #     파이어볼은 4개의 파이어볼로 나눠짐
    #     질량 = 합쳐진 파이어볼 질량합/5
    #     속력 합쳐진 파이어볼 속력합/ 합쳐진 파이어볼 개수
    #     합쳐진 파이어볼 방향 모두 홀수 or 짝수 -> 0, 2, 4 ,6 else 1, 3, 5, 7
    #     질량이 0인 파이어볼은 소멸
    for i in range(1, field_size+1):
        for j in range(1, field_size+1):
            fireballs = field[i][j]['next']
            if len(fireballs) < 2:
                field[i][j]['cur'] = field[i][j]['next']
                field[i][j]['next'] = []
            else:
                cur_fireballs = []
                cur_m, cur_s = 0, 0
                even_or_odd = fireballs[0][2] % 2
                d_diff = False
                for fireball in fireballs:
                    cur_m += fireball[0]
                    cur_s += fireball[1]
                    if even_or_odd != fireball[2] % 2:
                        d_diff = True
                cur_m = math.floor(cur_m/5)
                cur_s = math.floor(cur_s/len(fireballs))
                cur_d = None
                if d_diff:
                    cur_d = [1, 3, 5, 7]
                else:
                    cur_d = [0, 2, 4, 6]

                if cur_m > 0:
                    for d in cur_d:
                        cur_fireballs.append([cur_m, cur_s, d])

                field[i][j]['cur'] = cur_fireballs
                field[i][j]['next'] = []
    # print_field()
res = 0
for i in range(1, field_size + 1):
    for j in range(1, field_size + 1):
        if len(field[i][j]['cur']) == 0: continue
        for fireball in field[i][j]['cur']:
            res += fireball[0]
print(res)
