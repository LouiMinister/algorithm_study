# 주사위 윷놀이
from itertools import product

field = {
        0: (0,[1]),
        1: (2,[2]),
        2: (4,[3]),
        3: (6,[4]),
        4: (8,[5]),
        5: (10,[6, 101]),
        101: (13, [102]),
        102: (16, [103]),
        103: (19, [104]),
        6: (12, [7]),
        7: (14, [8]),
        8: (16, [9]),
        9: (18, [10]),
        10: (20, [11, 105]),
        105: (22, [106]),
        106: (24, [104]),
        11: (22, [12]),
        12: (24, [13]),
        13: (26, [14]),
        14: (28, [15]),
        15: (30, [16, 107]),
        107: (28, [108]),
        108: (27, [109]),
        109: (26, [104]),
        104: (25, [110]),
        110: (30, [111]),
        111: (35, [20]),
        16: (32, [17]),
        17: (34, [18]),
        18: (36, [19]),
        19: (38, [20]),
        20: (40, [21]),
        21: (0, [])
    }

dices = list(map(int, input().split()))

def simulation(order):
        pos = [0,0,0,0]
        res = 0
        for i in range(10):
                cur_turn = order[i]
                cur_dice = dices[i]
                cur_cell_score, next_cells = field.get(pos[cur_turn])
                if len(next_cells) == 0: return 0
                next_cell = next_cells[1] if len(next_cells) == 2 else next_cells[0]
                for _ in range(1,cur_dice):
                        next_next_cells = field[next_cell][1]
                        if len(next_next_cells) > 0:
                                next_cell = next_next_cells[0]
                        else:
                                next_cell = 21
                                break
                if next_cell != 21 and next_cell in pos: return 0
                pos[cur_turn] = next_cell
                res += field[next_cell][0]
        return res

candis = product([0,1,2,3], repeat=10)
res = 0
for candi in candis:
        res = max(res, simulation(list(candi)))
print(res)