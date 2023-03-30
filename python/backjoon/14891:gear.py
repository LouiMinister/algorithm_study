# 톱니바퀴

from collections import deque

class Gear:
    def __init__(self, steps):
        self.rightGear = None
        self.leftGear = None
        self.steps = deque(steps)

    def setLeftGear(self, gear):
        self.leftGear = gear

    def setRightGear(self, gear):
        self.rightGear = gear

    # direction 1: 시계방향, -1: 반시계 방향
    def turn_by_admin(self, direction):
        # 오른쪽 기어 돌리기
        if self.rightGear:
            self.rightGear.__turn_by_gear('L', self.steps[2], -direction)
        if self.leftGear:
            self.leftGear.__turn_by_gear('R', self.steps[-2], -direction)
        self.__rotate(direction)

    # 왼쪽, 오른쪽에서 / 어떤 스텝이 / 어떤 방향으로
    def __turn_by_gear(self, gear_from, step, direction):
        # N,S 극 같으면 탈출
        my_step = self.steps[2] if gear_from == 'R' else self.steps[-2]
        if my_step == step: return

        # 다른 기어도 회전
        affect_gear = self.leftGear if gear_from == 'R' else self.rightGear
        connected_step = self.steps[-2] if gear_from == 'R' else self.steps[2]
        if affect_gear:
            affect_gear.__turn_by_gear(gear_from, connected_step, -direction)

        # 자신 회전
        self.__rotate(direction)

    def __rotate(self, direction):
        if direction == 1:
            self.steps.appendleft(self.steps.pop())
        elif direction == -1:
            self.steps.append(self.steps.popleft())


gears = [Gear(map(int, input())) for _ in range(4)]
for i in range(4):
    if i - 1 >= 0:
        gears[i].leftGear = gears[i-1]
    if i + 1 < 4:
        gears[i].rightGear = gears[i+1]

N = int(input())
for _ in range(N):
    idx, direction = map(int, input().split(' '))
    gears[idx-1].turn_by_admin(direction)

res = 0
for i in range(4):
    res += gears[i].steps[0] * (2**i)
print(res)