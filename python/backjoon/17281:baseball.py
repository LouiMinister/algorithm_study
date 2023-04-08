from itertools import permutations


# 입력
N = int(input())
# play[이닝][선수]
play = [list(map(int, input().split(' '))) for _ in range(N)]


players_idx = [i for i in range(1,9)]
players_orders = permutations(players_idx)
result = 0
for players_order in players_orders:
    players_order = list(players_order)
    players_order = players_order[:3] + [0] + players_order[3:]

    # 다음에 플레이 할 유저 인덱스
    cur_player_idx = 0
    score = 0
    # 순서에 맞게 게임 진행
    for cur_round in range(N):
        out_cnt = 0
        field = [False] * 3 # 0 - 1루, 1 - 2루, 2 - 3루
        while out_cnt < 3:
            # 각 플레이어 순서대로 나와서 플레이
            # 플레이 결과에 따라 score나 field, out_cnt 업데이트
            cur_player = players_order[cur_player_idx]
            cur_play = play[cur_round][cur_player]
            if cur_play == 0:
                out_cnt += 1
            elif cur_play == 4:
                score += 1
                for f_i, player_exist in enumerate(field):
                    if player_exist:
                        score += 1
                        field[f_i] = False
            else:
                for f_i in range(2, -1, -1): # 필드 순회 2 ~ 0
                    player_on_field = field[f_i]
                    if player_on_field:
                        next_pos = f_i + cur_play
                        if next_pos > 2: # 3루 초과면
                            score += 1
                        else: # 3루 이하면
                            field[next_pos] = True
                        field[f_i] = False
                field[cur_play-1] = True # 타자 주루
            cur_player_idx = (cur_player_idx + 1) % 9
        # 라운드 종료
    # 게임 종료

    result = max(result, score)

print(result)
