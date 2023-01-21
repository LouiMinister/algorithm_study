# 왕실의 나이트
pos = input()
pos_x = ord(pos[0]) - ord('a')
pos_y = int(pos[1]) - 1
result = 0

for x, y in [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]:
    if 0 <= pos_x + x < 8 and 0 <= pos_y + y < 8:
        result += 1

print(result)